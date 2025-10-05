import ctypes
from ctypes import wintypes, c_void_p, structure, cfunctype, pointer, byref, create_string_buffer
import sys
import psutil

# load dlls
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
user32   = ctypes.WinDLL("user32", use_last_error=True)
gdi32    = ctypes.WinDLL("gdi32", use_last_error=True)
advapi32 = ctypes.WinDLL("advapi32", use_last_error=True)
psapi    = ctypes.WinDLL("psapi", use_last_error=True)
ntdll    = ctypes.WinDLL("ntdll", use_last_error=True)

# type aliases
byte    = ctypes.c_uint8
word    = ctypes.c_uint16
dword   = ctypes.c_uint32
qword   = ctypes.c_uint64
long_t  = ctypes.c_int32
ulong_t = ctypes.c_ulong
lpvoid  = c_void_p
handle  = wintypes.HANDLE
hwnd    = wintypes.HWND
hdc     = wintypes.HDC
hbitmap = wintypes.HANDLE
bool_t  = wintypes.BOOL

# pointer size
if sys.maxsize > 2**32:
    ptr_size = 8
    uint_ptr = ctypes.c_uint64
    int_ptr  = ctypes.c_int64
else:
    ptr_size = 4
    uint_ptr = ctypes.c_uint32
    int_ptr  = ctypes.c_int32

# structures
class memory_basic_information(structure):
    _fields_ = [
        ("base_address", lpvoid),
        ("allocation_base", lpvoid),
        ("allocation_protect", dword),
        ("region_size", ctypes.c_size_t),
        ("state", dword),
        ("protect", dword),
        ("type", dword)
    ]

class bitmap_file_header(structure):
    _fields_ = [
        ("bf_type", word),
        ("bf_size", dword),
        ("bf_reserved1", word),
        ("bf_reserved2", word),
        ("bf_off_bits", dword)
    ]

class bitmap_info_header(structure):
    _fields_ = [
        ("bi_size", dword),
        ("bi_width", long_t),
        ("bi_height", long_t),
        ("bi_planes", word),
        ("bi_bit_count", word),
        ("bi_compression", dword),
        ("bi_size_image", dword),
        ("bi_x_pels_per_meter", long_t),
        ("bi_y_pels_per_meter", long_t),
        ("bi_clr_used", dword),
        ("bi_clr_important", dword)
    ]

# resolve functions dynamically
class function_resolver:
    def __init__(self):
        self.cache = {}

    def _get_module(self, dll: str):
        h = kernel32.getmodulehandlew(dll)
        if not h: h = kernel32.loadlibraryw(dll)
        if not h: raise ctypes.WinError()
        return h

    def resolve(self, dll: str, func: str, restype=lpvoid, argtypes=None):
        key = (dll.lower(), func.lower())
        if key in self.cache:
            return self.cache[key]
        hmod = self._get_module(dll)
        addr = kernel32.getprocaddress(hmod, func.encode("ascii"))
        if not addr: raise ctypes.WinError()
        fn = cfunctype(restype, *(argtypes or []))(addr)
        self.cache[key] = fn
        return fn

resolver = function_resolver()

# api functions
virtual_alloc = resolver.resolve("kernel32.dll", "VirtualAlloc", restype=lpvoid, argtypes=[lpvoid, ctypes.c_size_t, dword, dword])
virtual_free  = resolver.resolve("kernel32.dll", "VirtualFree", restype=bool_t, argtypes=[lpvoid, ctypes.c_size_t, dword])
get_foreground_window = resolver.resolve("user32.dll", "GetForegroundWindow", restype=hwnd, argtypes=[])
get_window_text_w = resolver.resolve("user32.dll", "GetWindowTextW", restype=dword, argtypes=[hwnd, ctypes.c_wchar_p, dword])

read_process_memory  = resolver.resolve("kernel32.dll", "ReadProcessMemory", restype=bool_t,
                                        argtypes=[handle, lpvoid, lpvoid, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)])
write_process_memory = resolver.resolve("kernel32.dll", "WriteProcessMemory", restype=bool_t,
                                        argtypes=[handle, lpvoid, lpvoid, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)])

nt_read_virtual_memory = resolver.resolve("ntdll.dll", "NtReadVirtualMemory", restype=dword,
                                          argtypes=[handle, lpvoid, lpvoid, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)])
nt_write_virtual_memory = resolver.resolve("ntdll.dll", "NtWriteVirtualMemory", restype=dword,
                                           argtypes=[handle, lpvoid, lpvoid, ctypes.c_size_t, ctypes.POINTER(ctypes.c_size_t)])

# memory utils
class mem_utils:
    def __init__(self):
        self.kernel32 = kernel32
        self.ntdll = ntdll

    # process
    def open_process(self, pid, access=0x1F0FFF):
        h = kernel32.openprocess(access, False, pid)
        if not h: raise ctypes.WinError(ctypes.get_last_error())
        return h

    def find_process(self, name=None, window_title=None):
        hwnd_val = None
        pid_val = None

        if window_title:
            hwnd_val = get_foreground_window()
            buf = ctypes.create_unicode_buffer(512)
            get_window_text_w(hwnd_val, buf, 512)
            if window_title.lower() not in buf.value.lower(): hwnd_val = None

        if not hwnd_val and name:
            for proc in psutil.process_iter(["pid","name"]):
                if proc.info["name"].lower() == name.lower():
                    return None, proc.info["pid"]

        if hwnd_val:
            pid_d = wintypes.DWORD()
            kernel32.getwindowthreadprocessid(hwnd_val, byref(pid_d))
            pid_val = pid_d.value

        if not pid_val: raise ValueError("process not found")
        return hwnd_val, pid_val

    # memory
    def virtual_query(self, addr: int):
        mbi = memory_basic_information()
        if self.kernel32.virtualquery(lpvoid(addr), byref(mbi), ctypes.sizeof(mbi)) == 0:
            raise ctypes.WinError()
        return mbi

    def alloc(self, size: int, prot=0x40, type_=0x1000):
        addr = self.kernel32.virtualalloc(None, size, type_, prot)
        if not addr: raise ctypes.WinError()
        return addr

    def free(self, addr):
        if not self.kernel32.virtualfree(lpvoid(addr), 0, 0x8000): raise ctypes.WinError()

    # kernel32 read/write
    def rpm(self, process_handle, address, size):
        buf = ctypes.create_string_buffer(size)
        bytes_read = ctypes.c_size_t(0)
        if not read_process_memory(process_handle, lpvoid(address), buf, size, byref(bytes_read)):
            raise ctypes.WinError(ctypes.get_last_error())
        return buf.raw[:bytes_read.value]

    def wpm(self, process_handle, address, data: bytes):
        buf = ctypes.create_string_buffer(data)
        bytes_written = ctypes.c_size_t(0)
        if not write_process_memory(process_handle, lpvoid(address), buf, len(data), byref(bytes_written)):
            raise ctypes.WinError(ctypes.get_last_error())
        return bytes_written.value

    # nt read/write
    def nt_rpm(self, process_handle, address, size):
        buf = ctypes.create_string_buffer(size)
        bytes_read = ctypes.c_size_t(0)
        status = nt_read_virtual_memory(process_handle, lpvoid(address), buf, size, byref(bytes_read))
        if status != 0: raise OSError(f"ntreadvirtualmemory failed {status:#x}")
        return buf.raw[:bytes_read.value]

    def nt_wpm(self, process_handle, address, data: bytes):
        buf = ctypes.create_string_buffer(data)
        bytes_written = ctypes.c_size_t(0)
        status = nt_write_virtual_memory(process_handle, lpvoid(address), buf, len(data), byref(bytes_written))
        if status != 0: raise OSError(f"ntwritevirtualmemory failed {status:#x}")
        return bytes_written.value

# helper
def get_foreground_title(max_len=512):
    hwnd_val = get_foreground_window()
    buf = ctypes.create_unicode_buffer(max_len)
    length = get_window_text_w(hwnd_val, buf, max_len)
    return buf.value[:length]
