# DrexLib/__init__.py

"""
DrexLib - Drexxy's Hacking Library

Version: 0.0.1

This library contains various utilities to ease development, especially for hacking-related tasks.
It includes modules for:
- Internet functions
- Random utilities
- Windows-specific utilities
- Key validation
- Logging
- Text effects
- JSON handling

Requirements:
- Python 3.11+
- pip modules: cryptography, pywin32, requests
"""

# Import all classes and functions from the Drexlib.py file
from Drexlib.Drexlib import (
    internet, 
    rand_string, randint, 
    Windows, WindowsAPI, 
    KeyValidation, 
    logging, 
    fade, 
    JSON, 
    DEBUG, CONNECTED, VERSION, ADMIN, proc, written_mem, addresses, _read, SECRET_KEY, api
)

# Expose the classes, functions, and global variables directly to the package namespace
__all__ = [
    "internet", 
    "rand_string", "randint", 
    "Windows", "WindowsAPI", 
    "KeyValidation", 
    "logging", 
    "fade", 
    "JSON", 
    "DEBUG", "CONNECTED", "VERSION", "ADMIN", "proc", "written_mem", "addresses", "_read", "SECRET_KEY", "api"
]
