## Table of Contents

1. [Global Variables](#global-variables)
2. [Cheat Variables](#cheat-variables)
3. [Login Variables](#login-variables)
4. [Internet Class](#internet-class)
    1. [get_ip()](#get_ip)
    2. [check_internet()](#check_internet)
5. [Random Functions](#random-functions)
    1. [rand_string()](#rand_string)
    2. [randint()](#randint)
6. [Windows Utilities Class](#windows-utilities-class)
    1. [clear()](#clear)
    2. [run_command()](#run_command)
    3. [check_disk_space()](#check_disk_space)
    4. [list_running_processes()](#list_running_processes)
    5. [get_system_info()](#get_system_info)
    6. [shutdown_system()](#shutdown_system)
    7. [restart_system()](#restart_system)
7. [WindowsAPI Class](#windowsapi-class)
    1. [Kernel32 Functions](#kernel32-functions)
        1. [get_current_process()](#get_current_process)
        2. [close_handle()](#close_handle)
        3. [terminate_process()](#terminate_process)
    2. [Memory Management Functions](#memory-management-functions)
        1. [read_process_memory()](#read_process_memory)
        2. [write_process_memory()](#write_process_memory)
    3. [Thread Management Functions](#thread-management-functions)
        1. [create_thread()](#create_thread)
        2. [exit_thread()](#exit_thread)
8. [KeyValidation Class](#keyvalidation-class)
    1. [encrypt_data()](#encrypt_data)
    2. [decrypt_data()](#decrypt_data)
    3. [generate_key()](#generate_key)
    4. [validate_key()](#validate_key)
9. [Logging Class](#logging-class)
    1. [_get_current_time()](#_get_current_time)
    2. [log_info()](#log_info)
    3. [log_error()](#log_error)
    4. [log_success()](#log_success)
10. [Usage Example](#usage-example)

---

## Global Variables

- **DEBUG**: A boolean flag for enabling/disabling debug mode (default is `False`).
- **CONNECTED**: A boolean flag indicating connection status (default is `False`).
- **VERSION**: A string indicating the current version of the library (default is `"0.0.1"`).

## Cheat Variables

- **proc**: A variable to hold the process handle (default is an empty string).
- **written_mem**: A list to track written memory for logging purposes (default is an empty list).
- **addresses**: A dictionary holding memory addresses (default contains a sample `"localplayer"` address).
- **_read**: A temporary variable used for reading memory.

## Login Variables

- **_**: A placeholder for storing user input for username/key.
- **__**: A placeholder for storing user input for password.
- **SECRET_KEY**: A secret key for encryption (default is `b"DrexxyDaGoat69"`).
- **api**: A string representing the login API URL (default is `f"https://drexware.store/api/login/{VERSION}"`).

---

## Internet Class

### get_ip()

Fetches and returns the external IP address of the machine by calling `https://api.ipify.org?format=json`.

- **Returns**: The external IP address (string).
- **Exceptions**: Returns an error message if the request fails.

### check_internet()

Checks whether the machine is connected to the internet by attempting to access `https://www.google.com`.

- **Returns**: `True` if connected, `False` otherwise.

---

## Random Functions

### rand_string(length=16)

Generates and returns a random string of the specified length (default is 16).

- **Args**: `length` (int): The length of the random string to generate (default is 16).
- **Returns**: A random string consisting of ASCII letters.

### randint(low: int, high: int)

Returns a random integer between the specified low and high bounds (inclusive).

- **Args**: `low` (int), `high` (int): The range for the random integer.
- **Returns**: A random integer between `low` and `high`.

---

## Windows Utilities Class

### clear()

Clears the terminal screen based on the operating system (Windows: `cls`, other OS: `clear`).

### run_command(cmd: str, capture_output=False)

Executes a shell command. If `capture_output` is `True`, it returns the command output.

- **Args**: 
  - `cmd` (str): The command to execute.
  - `capture_output` (bool): Whether to capture and return the command's output (default is `False`).
- **Returns**: Command output if `capture_output` is `True`, otherwise `None`.

### check_disk_space(drive: str = "C:")

Checks the free and total space on the specified drive (default is `"C:"`).

- **Args**: 
  - `drive` (str): The drive letter (default is `"C:"`).
- **Returns**: A string indicating the available and total disk space in GB.

### list_running_processes()

Returns a list of currently running processes using the `tasklist` command.

- **Returns**: A string with the list of processes.

### get_system_info()

Retrieves and returns system information using the `systeminfo` command.

- **Returns**: A string containing system information.

### shutdown_system(delay)

Shuts down the system after the specified delay (in seconds).

- **Args**: `delay` (int): The delay in seconds before shutting down.

### restart_system(delay)

Restarts the system after the specified delay (in seconds).

- **Args**: `delay` (int): The delay in seconds before restarting.

---

## WindowsAPI Class

### Kernel32 Functions

#### get_current_process()

Retrieves the handle of the current process using `kernel32.dll`.

- **Returns**: Process handle.

#### close_handle(handle)

Closes a specified handle using `kernel32.dll`.

- **Args**: `handle` (HANDLE): The handle to close.
- **Returns**: `True` if successful, `False` if failed.

#### terminate_process(process_handle, exit_code)

Terminates a process using `kernel32.dll`.

- **Args**: 
  - `process_handle` (HANDLE): The process handle.
  - `exit_code` (UINT): The exit code for the process.
- **Returns**: `True` if successful, `False` if failed.

### Memory Management Functions

#### read_process_memory(process_handle, base_address, buffer, size, bytes_read)

Reads memory from a process using `kernel32.dll`.

- **Args**:
  - `process_handle` (HANDLE): The process handle.
  - `base_address` (LPVOID): The memory address to read from.
  - `buffer` (LPVOID): A buffer to store the read data.
  - `size` (SIZE_T): The number of bytes to read.
  - `bytes_read` (SIZE_T*): A pointer to store the number of bytes read.
- **Returns**: `True` if successful, `False` if failed.

#### write_process_memory(process_handle, base_address, buffer, size, bytes_written)

Writes memory to a process using `kernel32.dll`.

- **Args**:
  - `process_handle` (HANDLE): The process handle.
  - `base_address` (LPVOID): The memory address to write to.
  - `buffer` (LPVOID): The data to write.
  - `size` (SIZE_T): The number of bytes to write.
  - `bytes_written` (SIZE_T*): A pointer to store the number of bytes written.
- **Returns**: `True` if successful, `False` if failed.

### Thread Management Functions

#### create_thread(thread_attributes, stack_size, start_address, param, creation_flags)

Creates a new thread using `kernel32.dll`.

- **Args**:
  - `thread_attributes` (LPVOID): The thread attributes.
  - `stack_size` (DWORD): The stack size for the thread.
  - `start_address` (LPVOID): The function to start the thread.
  - `param` (LPVOID): A parameter to pass to the thread function.
  - `creation_flags` (DWORD): Flags for thread creation.
- **Returns**: Thread handle if successful, `None` if failed.

#### exit_thread(exit_code)

Exits the current thread using `kernel32.dll`.

- **Args**: `exit_code` (DWORD): The exit code for the thread.

---

## KeyValidation Class

### encrypt_data(data)

Encrypts the provided data using AES (CBC mode) with a randomly generated IV.

- **Args**: `data` (str): The data to encrypt.
- **Returns**: The encrypted data as a base64 encoded string.

### decrypt_data(encrypted_data)

Decrypts the provided base64 encoded encrypted data using AES (CBC mode) with the IV extracted from the data.

- **Args**: `encrypted_data` (str): The encrypted data (base64 encoded).
- **Returns**: The decrypted data (string).

### generate_key(expiration_seconds)

Generates an encrypted key that encodes the current timestamp and an expiration timestamp (in seconds).

- **Args**: `expiration_seconds` (int): The number of seconds after which the key expires.
- **Returns**: The encrypted key (base64 encoded).

### validate_key(encrypted_key)

Validates the provided encrypted key by decrypting it and checking if the expiration timestamp is valid (i.e., the key has not expired).

- **Args**: `encrypted_key` (str): The encrypted key (base64 encoded).
- **Returns**: `True` if the key is valid, `False` otherwise.

---

## Logging Class

### _get_current_time()

Returns the current timestamp in the format `[HH:MM:SS]`.

### log_info(message)

Logs an info message with the `[INFO]` prefix.

- **Args**: `message` (str): The message to log.

### log_error(message)

Logs an error message with the `[ERROR]` prefix.

- **Args**: `message` (str): The message to log.

### log_success(message)

Logs a success message with the `[SUCCESS]` prefix.

- **Args**: `message` (str): The message to log.

---

## Usage Example

```python
from drexlib import Internet, Windows, KeyValidation

# Check internet connection
if Internet.check_internet():
    print("Connected to the internet")
else:
    print("No internet connection")

# Generate a random string
random_str = rand_string(32)
print(f"Random String: {random_str}")

# Validate Key
key = "some_encrypted_key_here"
if KeyValidation.validate_key(key):
    print("Valid key")
else:
    print("Invalid key")

# Run a command
output = Windows.run_command("dir")
print(output)
```
