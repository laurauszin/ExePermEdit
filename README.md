# ExePermEdit - EXE Permissions Editor

**ExePermEdit** is a Windows utility with a graphical user interface (GUI) that allows you to edit file permissions of executable (.exe) files. It uses the built-in Windows `icacls` tool to grant, deny, or reset permissions.

---

## Features

- **Grant Full Control**: Give full permissions to an executable file.
- **Deny Execution**: Restrict users from executing the selected file.
- **Reset Permissions**: Reset the permissions of an executable to its default state.

---

## Requirements

- Windows OS
- Python 3.x
- Administrative privileges (required for changing permissions)

---

## Installation

1. **Install Python**: Ensure Python 3 is installed on your machine. You can download it from [Python's official website](https://www.python.org).
2. **Install Tkinter**: Tkinter is included with standard Python distributions. If missing, install using:
    ```bash
    pip install tk
    ```
3. **Save the Script**: Save the code as `exe_permissions_editor.py`.

---

## How to Use

1. Run the program:
   - Double-click on the Python file or run it in the terminal:
     ```bash
     python exe_permissions_editor.py
     ```

2. **Select an EXE File**:
   - Use the "Browse" button to choose an executable file.

3. **Choose Action**:
   - Click on:
     - **"Grant Full Control"** to give everyone full permissions.
     - **"Deny Execution"** to block execution of the file.
     - **"Reset Permissions"** to revert the file to its default permissions.

4. **Confirm Changes**:
   - You will see a success or error message indicating whether the permissions were updated.

---

## Notes

- **Admin Privileges**: This program requires administrator privileges to modify file permissions.
- **Caution**: Incorrect usage may cause access issues with important files. Use with care.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgements

- Built with **Tkinter** for GUI.
- Utilizes the Windows `icacls` tool for permission management.
