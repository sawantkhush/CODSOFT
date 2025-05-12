import tkinter as tk
import random
import string
from tkinter import ttk

def generate_password():
    length_str = length_entry.get()
    if not length_str.isdigit():
        password_var.set("Enter a valid number")
        return

    length = int(length_str)
    if length < 4:
        password_var.set("Min length is 4")
        return

    # Start progress bar animation
    progress_bar["value"] = 0
    root.after(50, animate_progress, 0, length)

def animate_progress(value, length):
    if value <= 100:
        progress_bar["value"] = value
        root.after(10, animate_progress, value + 5, length)
    else:
        show_password(length)

def show_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)
    update_password_display()

def update_password_display():
    if show_password_var.get():
        password_entry.config(show="")
    else:
        password_entry.config(show="*")

# GUI Setup
root = tk.Tk()
root.title("Enhanced Password Generator")
root.geometry("350x250")
root.resizable(False, False)

# Widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack(pady=5)

tk.Button(root, text="Generate Password", command=generate_password).pack(pady=10)

progress_bar = ttk.Progressbar(root, orient="horizontal", length=250, mode="determinate")
progress_bar.pack(pady=5)

tk.Label(root, text="Generated Password:").pack(pady=5)

password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=30)
password_entry.pack()

show_password_var = tk.BooleanVar()
tk.Checkbutton(root, text="Show Password", variable=show_password_var, command=update_password_display).pack(pady=5)

root.mainloop()
