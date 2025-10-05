# Documentation for cmemutils
## Functions:

### get_foreground_title(max_len=512)
Returns the title of the currently active window.  
**Arguments:**  
- `max_len` (int): Maximum number of characters to read from the window title.  
**Returns:** `str` containing the window title.

## Classes:

### type_utils
Utility class for type operations and helper functions.

#### is_64bit()
Checks if the system is 64-bit.  
**Returns:** `bool`

#### pack_int_le(val: int, size: int) -> bytes
Packs an integer into little-endian byte format.  
**Arguments:**  
- `val` (int): Integer value to pack.  
- `size` (int): Number of bytes to use.  
**Returns:** `bytes`

#### unpack_int_le(buf: bytes) -> int
Unpacks a little-endian byte buffer into an integer.  
**Arguments:**  
- `buf` (bytes): Buffer to unpack.  
**Returns:** `int`

#### make_buffer(size: int)
Creates a ctypes string buffer.  
**Arguments:**  
- `size` (int): Size of buffer.  
**Returns:** `ctypes.create_string_buffer`

#### safe_call(func, *args)
Calls a function and raises an error if it fails.  
**Arguments:**  
- `func`: Callable function.  
- `*args`: Arguments to pass to the function.  
**Returns:** Function result

### function_resolver
Resolves DLL functions dynamically and caches them.

#### resolve(dll: str, func: str, restype=c_void_p, argtypes=None)
Resolves a function from a DLL and returns a callable ctypes function.  
**Arguments:**  
- `dll` (str): DLL name.  
- `func` (str): Function name.  
- `restype` (ctypes type, optional): Return type. Defaults to `c_void_p`.  
- `argtypes` (list, optional): Argument types. Defaults to None.  
**Returns:** `ctypes` callable

### mem_utils
Provides memory manipulation functions for the current process.

#### virtual_query(addr: int)
Queries memory information for a given address.  
**Arguments:**  
- `addr` (int): Address to query.  
**Returns:** `memory_basic_information` structure

#### alloc(size: int, prot=0x40, type_=0x1000)
Allocates memory in the current process.  
**Arguments:**  
- `size` (int): Number of bytes to allocate.  
- `prot` (int): Memory protection flags (default: PAGE_EXECUTE_READWRITE).  
- `type_` (int): Allocation type (default: MEM_COMMIT).  
**Returns:** Address of allocated memory

#### free(addr)
Frees allocated memory.  
**Arguments:**  
- `addr` (int): Address of memory to free.  
**Returns:** None

### Structures

#### memory_basic_information
Structure for `VirtualQuery` results.  
Fields: `base_address`, `allocation_base`, `allocation_protect`, `region_size`, `state`, `protect`, `type`

#### bitmapfileheader
Structure representing a BMP file header.  
Fields: `bfType`, `bfSize`, `bfReserved1`, `bfReserved2`, `bfOffBits`

#### bitmapinfoheader
Structure representing a BMP info header.  
Fields: `biSize`, `biWidth`, `biHeight`, `biPlanes`, `biBitCount`, `biCompression`, `biSizeImage`, `biXPelsPerMeter`, `biYPelsPerMeter`, `biClrUsed`, `biClrImportant`

## Global Functions Exposed

### kernel32.dll
- `virtual_alloc(lpvoid, size, dword, dword)`  
- `virtual_free(lpvoid, dword, dword)`  
- `get_last_error()`

### user32.dll
- `get_foreground_window()`  
- `get_window_text_w(hwnd, c_wchar_p, dword)`  
- `lock_workstation()`

### gdi32.dll
- `create_compatible_dc(hdc)`  
- `create_compatible_bitmap(hdc, width, height)`  
- `select_object(hdc, handle)`  
- `bit_blt(hdc, x, y, w, h, hdc_src, sx, sy, rop)`  
- `delete_object(handle)`  
- `delete_dc(hdc)`

### advapi32.dll
- `reg_open_key_ex_w(handle, c_wchar_p, dword, dword, POINTER(handle))`  
- `reg_query_value_ex_w(handle, c_wchar_p, lpvoid, POINTER(dword), lpvoid, POINTER(dword))`  
- `reg_close_key(handle)`

### psapi.dll
- `enum_process_modules(handle, POINTER(handle), dword, POINTER(dword))`  
- `get_module_filename_w(handle, handle, c_wchar_p, dword)`

