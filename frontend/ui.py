import tkinter as tk
from tkinter import filedialog
import os
import subprocess
import sys

from backend.auth import authenticate
from backend.crypto import hash_pin
from backend.user_store import save_user

# ---------------- GLOBAL ----------------
selected_path = None

# ---------------- HELPERS ----------------
def open_path(path):
    if not path:
        return

    if sys.platform.startswith("win"):
        os.startfile(path)          # Windows
    elif sys.platform.startswith("darwin"):
        subprocess.call(["open", path])     # macOS
    else:
        subprocess.call(["xdg-open", path]) # Linux

def clear_status():
    status.set("")

# ---------------- BIOMETRIC LOGIN ----------------
def biometric_login():
    if authenticate("biometric"):
        open_path(selected_path)
        status.set("✔ ACCESS GRANTED")
    pin_entry.delete(0, tk.END)
    root.after(1200, clear_status)

# ---------------- PIN LOGIN ----------------
def pin_login():
    if authenticate("pin", pin_entry.get()):
        open_path(selected_path)
        status.set("✔ ACCESS GRANTED")
    pin_entry.delete(0, tk.END)
    root.after(1000, clear_status)

# ---------------- CREATE USER ----------------
def create_user():
    pin = new_pin_entry.get()
    confirm = confirm_pin_entry.get()

    if pin and pin == confirm:
        save_user(hash_pin(pin))
        status.set("✔ USER CREATED")

    new_pin_entry.delete(0, tk.END)
    confirm_pin_entry.delete(0, tk.END)
    root.after(1200, clear_status)

# ---------------- SELECT FILE / FOLDER ----------------
def choose_target():
    global selected_path
    selected_path = filedialog.askopenfilename() or filedialog.askdirectory()
    if selected_path:
        status.set("✔ TARGET SELECTED")
        root.after(1000, clear_status)

# ---------------- UI ----------------
root = tk.Tk()
root.title("SECURE FILE ACCESS")
root.geometry("420x420")
root.resizable(False, False)

status = tk.StringVar()

tk.Label(root, text="Biometric Login", font=("Arial", 12, "bold")).pack(pady=5)
tk.Button(root, text="Fingerprint / Iris Login", width=30, command=biometric_login).pack()

tk.Label(root, text="PIN Login", font=("Arial", 12, "bold")).pack(pady=5)
pin_entry = tk.Entry(root, show="*", width=25)
pin_entry.pack()
tk.Button(root, text="Login with PIN", width=30, command=pin_login).pack(pady=5)

tk.Label(root, text="Create New User", font=("Arial", 12, "bold")).pack(pady=10)
new_pin_entry = tk.Entry(root, show="*", width=25)
new_pin_entry.pack()
confirm_pin_entry = tk.Entry(root, show="*", width=25)
confirm_pin_entry.pack()
tk.Button(root, text="Create User", width=30, command=create_user).pack(pady=5)

tk.Label(root, text="Protected File / Folder", font=("Arial", 12, "bold")).pack(pady=10)
tk.Button(root, text="Select File or Folder", width=30, command=choose_target).pack()

tk.Label(root, textvariable=status, fg="green").pack(pady=15)
