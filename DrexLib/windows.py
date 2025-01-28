import math
import time
import os
import string
import random
import subprocess
import threading
import json
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend
import base64
import ctypes
from ctypes import wintypes
import win32api
import win32process
import win32con
from win32api import OpenProcess



class WindowsAPI:
        def __init__(self):
            # Load kernel32 and user32 DLLs
            self.kernel32 = ctypes.WinDLL('kernel32.dll')
            self.user32 = ctypes.WinDLL('user32.dll')
        def FindWindowA(self,windowtitle):
             
    
    

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

   