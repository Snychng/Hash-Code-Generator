# gui.py

import tkinter as tk
from tkinter import ttk
from ttkbootstrap import Style
from functions import on_generate_password, on_validate_password, open_webpage

style = Style('lumen')  

root = style.master
root.title("Password Generator and Validator")

# Configure rows and columns
for i in range(5):
    root.grid_rowconfigure(i, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

date_label = ttk.Label(root, text="Date:")
date_label.grid(row=0, column=0, sticky='nsew', padx=10, pady=10)

date_entry = ttk.Entry(root)
date_entry.insert(0, "YYYYMMDD")
date_entry.config(foreground="grey")
date_entry.grid(row=0, column=1, sticky='nsew', padx=10, pady=10)

def on_entry_click(event):
    """function that gets called whenever entry is clicked"""
    if date_entry.get() == 'YYYYMMDD':
        date_entry.delete(0, "end") # delete all the text in the entry
        date_entry.insert(0, '') # Insert blank for user input
        date_entry.config(foreground="black")

def on_focusout(event):
    if date_entry.get() == '':
        date_entry.insert(0, 'YYYYMMDD')
        date_entry.config(foreground="grey")

date_entry.bind('<FocusIn>', on_entry_click)
date_entry.bind('<FocusOut>', on_focusout)


password_label = ttk.Label(root, text="Generated Password:")
password_label.grid(row=1, column=0, sticky='nsew', padx=10, pady=10)

password_entry = ttk.Entry(root)
password_entry.configure(state='readonly')
password_entry.grid(row=1, column=1, sticky='nsew', padx=10, pady=10)

input_password_label = ttk.Label(root, text="Input Password:")
input_password_label.grid(row=2, column=0, sticky='nsew', padx=10, pady=10)

input_password_entry = ttk.Entry(root)
input_password_entry.grid(row=2, column=1, sticky='nsew', padx=10, pady=10)

generate_password_button = ttk.Button(root, text="Generate Password", command=lambda: on_generate_password(password_entry))
generate_password_button.grid(row=3, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

validate_password_button = ttk.Button(root, text="Validate Password", command=lambda: on_validate_password(date_entry, input_password_entry))
validate_password_button.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=10, pady=10)

button = ttk.Button(root, text="📍", command=open_webpage)
button.grid(row=100, column=0, sticky='sw')  

root.mainloop()