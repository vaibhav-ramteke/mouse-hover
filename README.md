# Mouse Hover Automation

This project automates mouse movement in a square pattern using Python. It can be used to prevent your computer from going idle or to simulate activity.

> Want to appear "always available" on Teams, even when you're grabbing coffee? This project has your back. Your boss will think you never left your desk!

## Features

- Moves the mouse cursor in a square loop (right, down, left, up).
- Runs continuously until you stop it with `Ctrl+C`.
- Simple batch script to activate the Python virtual environment and run the script.

## Requirements

- Python 3.x
- [pyautogui](https://pypi.org/project/pyautogui/) library
- Windows OS (for the provided batch file)

## Setup

1. **Clone or download this repository.**
2. **Create a virtual environment (optional but recommended):**
   ```sh
   python -m venv .venv
   ```
3. **Activate the virtual environment:**
   - On Windows:
     ```sh
     .venv\Scripts\activate
     ```
4. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

## Usage

### Using the Batch File

Double-click `hover.bat` to activate the virtual environment and start the mouse hover script.

### Using Python Directly

Alternatively, run the script manually:
```sh
python hover.py
```

To stop the script, press `Ctrl+C` in the terminal.

## Creating a Desktop Shortcut

To make it even easier to use, you can create a shortcut to `hover.bat` on your desktop:

1. Right-click on `hover.bat` in your project folder.
2. Select **Show more options** (or just **Send to** on some Windows versions).
3. Click **Send to > Desktop (create shortcut)**.
4. You will now have a shortcut on your desktop. Double-click it anytime to start the mouse hover script.

## Notes

- Make sure your mouse is not needed for other tasks while the script is running.
- The script will keep your system active as long as it runs.

---
