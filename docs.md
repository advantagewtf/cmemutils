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

- **DEBUG**: Boolean flag to enable/disable debug mode (default: `False`).
- **CONNECTED**: Boolean flag for connection status (default: `False`).
- **VERSION**: Current version of the library (default: `"0.0.1"`).

## Cheat Variables

- **proc**: Stores the process handle (default: empty string).
- **written_mem**: Tracks written memory (default: empty list).
- **addresses**: Dictionary of memory addresses (default: contains sample `"localplayer"` address).
- **_read**: Temporary variable for reading memory.

## Login Variables

- **_**: Placeholder for username/key input.
- **__**: Placeholder for password input.
- **SECRET_KEY**: Secret key for encryption (default: `b"DrexxyDaGoat69"`).
- **api**: Login API URL (default: `f"https://drexware.store/api/login/{VERSION}"`).

---

## Internet Class

### get_ip()

Fetches and returns the external IP address via `https://api.ipify.org?format=json`.

- **Returns**: External IP address (string).
- **Exceptions**: Returns error message if request fails.

### check_internet()

Checks internet connectivity by accessing `https://www.google.com`.

- **Returns**: `True` if connected, `False` otherwise.

---

## Random Functions

### rand_string(length=16)

Generates a random string of specified length (default: 16).

- **Args**: `length` (int): Length of the random string (default: 16).
- **Returns**: Random string of ASCII letters.

### randint(low: int, high: int)

Returns a random integer between `low` and `high`.

- **Args**: `low` (int), `high` (int): Range for random integer.
- **Returns**: Random integer between `low` and `high`.

---

## Windows Utilities Class

### clear()

Clears the terminal screen (`cls` for Windows, `clear` for others).

### run_command(cmd: str, capture_output=False)

Executes a shell command; returns output if `capture_output` is `True`.

- **Args**: 
  - `cmd` (str): Command to execute.
  - `capture_output` (bool): Capture command output (default: `False`).
- **Returns**: Command output if `capture_output` is `True`.

### check_disk_space(drive: str = "C:")

Checks disk space on specified drive (default: `"C:"`).

- **Args**: 
  - `drive` (str): Drive letter (default: `"C:"`).
- **Returns**: Available and total disk space in GB.

### list_running_processes()

Returns a list of currently running processes.

- **Returns**: List of running processes (string).

### get_system_info()

Retrieves system information.

- **Returns**: System information (string).

### shutdown_system(delay)

Shuts down system after specified delay (seconds).

- **Args**: `delay` (int): Delay before shutdown.

### restart_system(delay)

Restarts system after specified delay (seconds).

- **Args**: `delay` (int): Delay before restart.

---

## WindowsAPI Class

### Kernel32 Functions

#### get_current_process()

Retrieves current process handle.

- **Returns**: Process handle.

#### close_handle(handle)

Closes specified handle.

- **Args**: `handle` (HANDLE): Handle to close.
- **Returns**: `True` if successful, `False` if failed.

#### terminate_process(process_handle, exit_code)

Terminates a process.

- **Args**: 
  - `process_handle` (HANDLE): Process handle.
  - `exit_code` (UINT): Exit code.
- **Returns**: `True` if successful, `False` if failed.

### Memory Management Functions

#### read_process_memory(process_handle, base_address, buffer, size, bytes_read)

Reads memory from a process.

- **Args**:
  - `process_handle` (HANDLE): Process handle.
  - `base_address` (LPVOID): Memory address.
  - `buffer` (LPVOID): Buffer for data.
  - `size` (SIZE_T): Bytes to read.
  - `bytes_read` (SIZE_T*): Pointer to bytes read.
- **Returns**: `True` if successful, `False` if failed.

#### write_process_memory(process_handle, base_address, buffer, size, bytes_written)

Writes memory to a process.

- **Args**:
  - `process_handle` (HANDLE): Process handle.
  - `base_address` (LPVOID): Memory address.
  - `buffer` (LPVOID): Data to write.
  - `size` (SIZE_T): Bytes to write.
  - `bytes_written` (SIZE_T*): Pointer to bytes written.
- **Returns**: `True` if successful, `False` if failed.

### Thread Management Functions

#### create_thread(thread_attributes, stack_size, start_address, param, creation_flags)

Creates a new thread.

- **Args**:
  - `thread_attributes` (LPVOID): Thread attributes.
  - `stack_size` (DWORD): Stack size.
  - `start_address` (LPVOID): Start function.
  - `param` (LPVOID): Function parameter.
  - `creation_flags` (DWORD): Creation flags.
- **Returns**: Thread handle if successful.

#### exit_thread(exit_code)

Exits the current thread.

- **Args**: `exit_code` (DWORD): Exit code.

---

## KeyValidation Class

### encrypt_data(data)

Encrypts data using AES (CBC mode) with a random IV.

- **Args**: `data` (str): Data to encrypt.
- **Returns**: Encrypted data (base64).

### decrypt_data(encrypted_data)

Decrypts base64 encoded data using AES (CBC mode).

- **Args**: `encrypted_data` (str): Encrypted data (base64).
- **Returns**: Decrypted data (string).

### generate_key(expiration_seconds)

Generates an encrypted key with expiration timestamp.

- **Args**: `expiration_seconds` (int): Key expiration in seconds.
- **Returns**: Encrypted key (base64).

### validate_key(encrypted_key)

Validates encrypted key for expiration.

- **Args**: `encrypted_key` (str): Encrypted key (base64).
- **Returns**: `True` if valid, `False` otherwise.

---

## Logging Class

### _get_current_time()

Returns current timestamp `[HH:MM:SS]`.

### log_info(message)

Logs info message with `[INFO]` prefix.

- **Args**: `message` (str): Message to log.

### log_error(message)

Logs error message with `[ERROR]` prefix.

- **Args**: `message` (str): Message to log.

### log_success(message)

Logs success message with `[SUCCESS]` prefix.

- **Args**: `message` (str): Message to log.

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
