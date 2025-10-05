# cmemutils

cmemutils — simple, focused Python utilities for working with process memory and offsets.  
Created by **advantagewtf** to provide small, reusable helpers for educational, research, and development purposes.

---

> ⚠️ **IMPORTANT — Responsible use only**  
> This project is intended **for educational and research purposes only** (learning about OS internals, debugging, testing tools you own, reverse-engineering for interoperability, etc.).  
> **Do not** use this code to break terms of service, cheat in multiplayer games, or otherwise violate laws or rules. The author and maintainers are **not** responsible for bans, account suspensions, or other penalties resulting from misuse.

---

# Table of contents
- Overview
- Features
- Requirements
- Installation
- Quick start
- API
- Examples
- Testing
- Contributing
- Roadmap
- License
- Support & Contact
- Disclaimer

---

# Overview
`cmemutils` is a small collection of Python helpers that make common memory- and offset-related tasks easier:
- process discovery and lightweight process handles
- reading/writing primitive values and blobs
- helpers for dealing with module bases and offsets
- utilities for parsing and converting offset files (JSON / CSV)

The aim is clarity and portability — each utility is simple and documented so it can be composed into larger debugging or tooling workflows.

---

# Features
- Enumerate running processes and modules
- Open a process handle (cross-platform considerations documented)
- Read and write bytes and primitives (ints, floats) through a simple API
- Resolve module base address and compute absolute addresses from offsets
- Load/save offset maps (JSON) and provide convenience conversion helpers
- Small, dependency-light footprint

---

# Requirements
- Python 3.9+ recommended
- Platform-specific dependencies may be required for low-level process access (see **Platform notes** below)
- No heavy external frameworks required for the core helpers

**Platform notes**
- Some operations (open process, read/write memory) require elevated privileges on modern OSes and/or platform-specific APIs. See the documentation for platform behavior and examples.

---

