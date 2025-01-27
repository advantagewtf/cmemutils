from ctypes import wintypes
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
import win32api
import win32process
import win32con
from win32api import OpenProcess
import requests

"""
-----
Drexxys Hacking Libary

Built to create tools and just ease the python expirience

------

necessities:
python 3.11.X
pip modules: cryptography pywin32 requests

"""


# --- Global variables ---

DEBUG = False
CONNECTED = False
VERSION = "1.0.0"
ADMIN = False

# --- Memory ----

proc = "" # handle to the process
written_mem = [] # to keep track for logging

# --- Login ---

_ = "" #user input for the username / key
__ = "" #user input for a password (usually not needed)
SECRET_KEY = b"DrexxyDaGoat69"
api = f"https://drexware.store/api/login/{VERSION}" 

#        ^^^^ drexware api 

# --- Internet functions ---
class internet:
	@staticmethod
	def get_ip() -> str:
	        """Returns the external IP address of the machine."""
	        try:
	            response = requests.get("https://api.ipify.org?format=json")
	            ip_info = response.json()
	            return ip_info.get("ip", "Unable to fetch IP")
	        except requests.RequestException as e:
	            return f"Error getting external IP: {e}"
	@staticmethod
	def check_internet() -> bool:
	        """Checks if the machine is connected to the internet."""
	        try:
	            requests.get("https://www.google.com", timeout=5)
	            return True
	        except requests.RequestException:
	            return False
# --- Random functions ---
def randint(low: int, high: int) -> int:
    return random.randint(low, high)
	
def rand_string(length=16) -> str:
    """
    Generate a random string of specified length using ASCII letters.

    Args:
        length (int): The length of the random string to generate. Defaults to 16.

    Returns:
        str: A randomly generated string of the specified length.
    """
    rand_str = ""
    for i in range(length):
        rand_str += random.choice(string.ascii_letters)
    return rand_str


# --- Windows Utilities ---
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


def delay(seconds: int):
    time.sleep(seconds)

# --- Key validation ---

class KeyValidation:
    def __init__(self, secret_key):
        self.secret_key = secret_key

    def encrypt_data(self, data):
        iv = os.urandom(16)
        cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padding_length = 16 - (len(data) % 16)
        data += chr(padding_length) * padding_length
        encrypted_data = encryptor.update(data.encode()) + encryptor.finalize()
        return base64.b64encode(iv + encrypted_data).decode()

    def decrypt_data(self, encrypted_data):
        encrypted_data = base64.b64decode(encrypted_data)
        iv = encrypted_data[:16]
        encrypted_data = encrypted_data[16:]
        cipher = Cipher(algorithms.AES(self.secret_key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()
        padding_length = ord(decrypted_data[-1:])
        return decrypted_data[:-padding_length].decode()

    def generate_key(self, expiration_seconds):
        timestamp = int(time.time())
        expiration_timestamp = timestamp + expiration_seconds
        key_data = f"{timestamp},{expiration_timestamp}"
        encrypted_key = self.encrypt_data(key_data)
        return encrypted_key

    def validate_key(self, encrypted_key):
        try:
            decrypted_key = self.decrypt_data(encrypted_key)
            current_timestamp = int(time.time())
            timestamp, expiration_timestamp = map(int, decrypted_key.split(','))
            if current_timestamp > expiration_timestamp:
                return False
            return True
        except Exception:
            return False
			
# --- logging ---
class logging:

    @staticmethod
    def _get_current_time() -> str:
        """Returns the current timestamp formatted as [HH:MM:SS]"""
        return time.strftime("%H:%M:%S", time.localtime())
    
    @staticmethod
    def _get_color_for_log(log_type: str) -> str:
        """Returns the corresponding color for a log type."""
        if log_type == "+":
            return "\033[38;2;0;255;0m"  # Green for success
        elif log_type == "!":
            return "\033[38;2;255;0;0m"  # Red for error
        else:
            return "\033[38;2;255;255;255m"  # White for regular log

    @staticmethod
    def log(log_type: str, message: str):
        global DEBUG
        if DEBUG:
            if log_type != " ":
                timestamp = logging._get_current_time()
                color = logging._get_color_for_log(log_type)
                reset_color = "\033[0m"  # Reset color after log message
                log_message = f"[{log_type}] {timestamp}: {message}"
                print(f"{color}{log_message}{reset_color}")
            else:
                # For normal logs, just print the message without timestamp and brackets
                color = logging._get_color_for_log(log_type)
                reset_color = "\033[0m"
                print(f"{color}{message}{reset_color}")

    @staticmethod
    def success(message: str):
        """Logs a success message."""
        logger.log("+", message)
    
    @staticmethod
    def error(message: str):
        """Logs an error message."""
        logger.log("!", message)
    
    @staticmethod
    def info(message: str):
        """Logs a regular info message."""
        logger.log(" ", message)


# --- text utilities ---
class fade:
    @staticmethod
    def random(text: str) -> str:
        faded = ""
        for line in text.splitlines():
            for character in line:
                faded += (f"\033[38;2;{randint(0,255)};{randint(0,255)};{randint(0,255)}m{character}\033[0m")
            faded += "\n"
        return faded

    @staticmethod
    def greenblue(text: str) -> str:
        faded = ""
        blue = 100
        for line in text.splitlines():
            faded += (f"\033[38;2;0;255;{blue}m{line}\033[0m\n")
            if blue != 255:
                blue += 15
                if blue > 255:
                    blue = 255
        return faded

    @staticmethod
    def redyellow(text: str) -> str:
        faded = ""
        yellow = 255
        for line in text.splitlines():
            faded += (f"\033[38;2;255;{yellow};0m{line}\033[0m\n")
            if yellow != 255:
                yellow -= 15
                if yellow < 0:
                    yellow = 0
        return faded

    @staticmethod
    def rainbow(text: str) -> str:
        faded = ""
        color_cycle = [(255, 0, 0), (255, 127, 0), (255, 255, 0), (0, 255, 0), (0, 0, 255), (75, 0, 130), (238, 130, 238)]
        color_index = 0
        for line in text.splitlines():
            for character in line:
                color = color_cycle[color_index]
                faded += f"\033[38;2;{color[0]};{color[1]};{color[2]}m{character}\033[0m"
                color_index = (color_index + 1) % len(color_cycle)
            faded += "\n"
        return faded

# --- Json class ---
class JSON:

    @staticmethod
    def decode(json_data: str) -> dict:
        """Decodes a JSON string into a Python dictionary."""
        try:
            return json.loads(json_data)
        except json.JSONDecodeError as e:
            return f"Error decoding JSON: {e}"

    @staticmethod
    def dump(data: dict, file_path: str) -> str:
        """Dumps a Python dictionary into a JSON file."""
        try:
            with open(file_path, 'w', encoding='utf-8') as json_file:
                json.dump(data, json_file, ensure_ascii=False, indent=4)
            return f"JSON data successfully written to {file_path}"
        except Exception as e:
            return f"Error writing JSON to file: {e}"

    @staticmethod
    def load(file_path: str) -> dict:
        """Loads a JSON file and returns it as a Python dictionary."""
        try:
            with open(file_path, 'r', encoding='utf-8') as json_file:
                return json.load(json_file)
        except Exception as e:
            return f"Error loading JSON file: {e}"

