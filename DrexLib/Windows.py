from imports import *
class Windows:
    @staticmethod
    def clear():
     os.system("cls" if os.name == "nt" else "clear")

    @staticmethod
    def run_command(cmd: str, capture_output=False):
	    if capture_output:
	        result = subprocess.run(cmd, shell=True, capture_output=True, text=True)
	        return result.stdout
	    else:
	        os.system(cmd)
    @staticmethod
    def check_disk_space(drive: str = "C:") -> str:
        try:
            result = subprocess.check_output(f"wmic logicaldisk where \"DeviceID='{drive}'\" get FreeSpace,Size", shell=True)
            lines = result.decode("utf-8").splitlines()
            free_space, total_space = map(int, lines[1].split())
            free_space_gb = free_space / (1024 ** 3)
            total_space_gb = total_space / (1024 ** 3)
            return f"Free space: {free_space_gb:.2f} GB out of {total_space_gb:.2f} GB on drive {drive}"
        except Exception as e:
            return f"Error checking disk space: {e}"

    @staticmethod
    def list_running_processes() -> str:
        try:
            result = subprocess.check_output("tasklist", shell=True)
            return result.decode("utf-8")
        except Exception as e:
            return f"Error listing processes: {e}"

    @staticmethod
    def get_system_info() -> str:
        try:
            result = subprocess.check_output("systeminfo", shell=True)
            return result.decode("utf-8")
        except Exception as e:
            return f"Error retrieving system info: {e}"

    @staticmethod
    def shutdown_system(delay) -> None:
        time.sleep(delay)
        os.system("shutdown /s /f /t 0")

    @staticmethod
    def restart_system(delay) -> None:
        time.sleep(delay)
        os.system("shutdown /r /f /t 0")

class WindowsAPI:
    def __init__(self):
        # Load kernel32 and user32 DLLs
        self.kernel32 = ctypes.WinDLL('kernel32.dll')
        self.user32 = ctypes.WinDLL('user32.dll')

    # Kernel32 Functions
    def get_current_process(self):
        """Gets the current process handle using kernel32.dll"""
        self.kernel32.GetCurrentProcess.argtypes = []
        self.kernel32.GetCurrentProcess.restype = wintypes.HANDLE
        return self.kernel32.GetCurrentProcess()
		
   
    def close_handle(self, handle):
        """Closes a handle using kernel32.dll"""
        self.kernel32.CloseHandle.argtypes = [wintypes.HANDLE]
        self.kernel32.CloseHandle.restype = wintypes.BOOL
        return self.kernel32.CloseHandle(handle)

   

    def terminate_process(self, process_handle, exit_code):
        """Terminates a process using kernel32.dll"""
        self.kernel32.TerminateProcess.argtypes = [wintypes.HANDLE, wintypes.UINT]
        self.kernel32.TerminateProcess.restype = wintypes.BOOL
        return self.kernel32.TerminateProcess(process_handle, exit_code)

    # Memory Management Functions
   
    def read_process_memory(self, process_handle, base_address, buffer, size, bytes_read):
        """Reads memory from a process using kernel32.dll"""
        self.kernel32.ReadProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPVOID,
                                                   wintypes.SIZE_T, ctypes.POINTER(wintypes.SIZE_T)]
        self.kernel32.ReadProcessMemory.restype = wintypes.BOOL
        return self.kernel32.ReadProcessMemory(process_handle, base_address, buffer, size, bytes_read)

    def write_process_memory(self, process_handle, base_address, buffer, size, bytes_written):
        """Writes memory to a process using kernel32.dll"""
        self.kernel32.WriteProcessMemory.argtypes = [wintypes.HANDLE, wintypes.LPVOID, wintypes.LPVOID,
                                                    wintypes.SIZE_T, ctypes.POINTER(wintypes.SIZE_T)]
        self.kernel32.WriteProcessMemory.restype = wintypes.BOOL
        return self.kernel32.WriteProcessMemory(process_handle, base_address, buffer, size, bytes_written)

  
    # Thread management
    def create_thread(self, thread_attributes, stack_size, start_address, param, creation_flags):
        """Creates a thread using kernel32.dll"""
        self.kernel32.CreateThread.argtypes = [wintypes.LPVOID, wintypes.DWORD, wintypes.LPVOID, wintypes.LPVOID,
                                              wintypes.DWORD, ctypes.POINTER(wintypes.DWORD)]
        self.kernel32.CreateThread.restype = wintypes.HANDLE
        return self.kernel32.CreateThread(thread_attributes, stack_size, start_address, param, creation_flags, None)

    def exit_thread(self, exit_code):
        """Exits the current thread using kernel32.dll"""
        self.kernel32.ExitThread.argtypes = [wintypes.DWORD]
        self.kernel32.ExitThread.restype = None
        self.kernel32.ExitThread(exit_code)
