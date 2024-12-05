==============
SemprexControl
==============

Python program for controlling lab stage made by Semprex

# Microscope Stage Controller

A Python-based interface to control a microscope stage using `samc.dll`.

## Setup
1. Create and activate the virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage
- Use the wrapper functions in `samc_wrapper.py` to interact with `samc.dll`.
- Example:
    ```python
    from src.samc_wrapper import set_addr

    set_addr(1, 38400)
    ```
