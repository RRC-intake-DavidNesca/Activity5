# Sports Application – Activity 5

## Overview

The Sports Application is a small desktop program used to demonstrate classes, docstrings, help file generation, and software distribution in COMP‑2327 Intermediate Software Development.

The program displays a simple **Sports League** window that shows a list of players (name, age, position) and includes a **Show Message** button. The window is built using the PySide6 GUI library, and the rest of the application logic is implemented using the League, Team, Player and SportsApp classes.

---

## Files and Folders

- `sports_application.py`  
  Client program that starts the Sports Application GUI.

- `league/`, `team/`, `player/`, `sports_app/`  
  Packages that contain the `League`, `Team`, `Player`, and `SportsApp` classes.

- `source/`  
  Sphinx configuration and index files used to generate the HTML help files.

- `build/html/`  
  Output folder for the generated Sphinx HTML documentation.

- `dist/sports_application/`  
  Folder created by PyInstaller containing the standalone `sports_application.exe` and its support files.

- `installer/`  
  Contains the Inno Setup installer script, license and information files, and the final installer executable:
  - `license.txt`
  - `before.txt`
  - `after.txt`
  - `SportsApplication-installer.iss`
  - `SportsApplication-installer.exe`

---

## System Requirements

To **run the installed application**:

- Windows operating system.

To **run the program from source** or rebuild the project:

- Python 3.x
- PySide6 (installed with `pip install PySide6`)
- Sphinx (installed with `pip install sphinx`)
- PyInstaller (installed with `pip install pyinstaller`)
- Inno Setup (installed separately) for rebuilding the installer

---

## Installing the Sports Application

1. Open the `installer` folder inside the Activity5 project:
   ```text
   Activity5\installer\
