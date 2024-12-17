import tkinter as tk
from tkinter import filedialog, messagebox
import subprocess
import os

class EXEPermissionsEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("ExePermEdit - EXE Permissions Editor")
        self.root.geometry("500x300")
        
        # File Path
        self.file_path = tk.StringVar()
        
        # GUI Components
        self.create_widgets()
    
    def create_widgets(self):
        # Header Label
        header_label = tk.Label(self.root, text="EXE Permissions Editor", font=("Arial", 16))
        header_label.pack(pady=10)

        # File Path Entry
        tk.Label(self.root, text="Select EXE File:").pack()
        file_entry = tk.Entry(self.root, textvariable=self.file_path, width=50)
        file_entry.pack(padx=10, pady=5)
        
        # Browse Button
        browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        browse_button.pack()

        # Permissions Buttons
        tk.Label(self.root, text="Choose Action:").pack(pady=10)
        allow_button = tk.Button(self.root, text="Grant Full Control", command=self.grant_full_control)
        allow_button.pack(pady=5)
        deny_button = tk.Button(self.root, text="Deny Execution", command=self.deny_execution)
        deny_button.pack(pady=5)
        reset_button = tk.Button(self.root, text="Reset Permissions", command=self.reset_permissions)
        reset_button.pack(pady=5)

        # Footer
        footer_label = tk.Label(self.root, text="Use with caution! Requires admin privileges.", font=("Arial", 10))
        footer_label.pack(pady=10)
    
    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
        if file_path:
            self.file_path.set(file_path)
    
    def run_icacls_command(self, args):
        try:
            if not os.path.isfile(self.file_path.get()):
                messagebox.showerror("Error", "Please select a valid EXE file.")
                return
            subprocess.run(args, check=True, shell=True)
            messagebox.showinfo("Success", "Permissions updated successfully.")
        except subprocess.CalledProcessError:
            messagebox.showerror("Error", "Failed to update permissions. Run as Administrator.")
    
    def grant_full_control(self):
        file = self.file_path.get()
        args = f'icacls "{file}" /grant Everyone:F'
        self.run_icacls_command(args)
    
    def deny_execution(self):
        file = self.file_path.get()
        args = f'icacls "{file}" /deny Everyone:X'
        self.run_icacls_command(args)
    
    def reset_permissions(self):
        file = self.file_path.get()
        args = f'icacls "{file}" /reset'
        self.run_icacls_command(args)

if __name__ == "__main__":
    root = tk.Tk()
    app = EXEPermissionsEditor(root)
    root.mainloop()
