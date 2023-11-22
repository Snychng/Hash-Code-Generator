# functions.py

import hashlib
import datetime
import os
import pickle
from collections import OrderedDict
from tkinter import messagebox
import webbrowser

DATA_FILE = 'password_data.pkl'

def generate_password(input_date, salt):
    hash_object = hashlib.pbkdf2_hmac('sha256', input_date.encode(), salt, 100000)
    hex_dig = hash_object.hex()
    password = hex_dig[:7]
    return password

def save_password_salt(date, password, salt):
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'rb') as f:
            data = pickle.load(f)
    else:
        data = OrderedDict()
    if date not in data:
        data[date] = []
    data[date].append({'password': password, 'salt': salt})

    while len(data) > 7:
        data.popitem(last=False)

    with open(DATA_FILE, 'wb') as f:
        pickle.dump(data, f)

def load_password_salt(date):
    with open(DATA_FILE, 'rb') as f:
        data = pickle.load(f)
    if date in data:
        return data[date]
    else:
        return None

def on_generate_password(password_entry):
    today = datetime.datetime.now().strftime('%Y%m%d')
    salt = os.urandom(16)
    password = generate_password(today, salt)
    save_password_salt(today, password, salt)
    password_entry.configure(state='normal')
    password_entry.delete(0, 'end')
    password_entry.insert(0, password)
    password_entry.configure(state='readonly')

def on_validate_password(date_entry, input_password_entry):
    input_date = date_entry.get()
    input_password = input_password_entry.get()
    password_salt_list = load_password_salt(input_date)
    if password_salt_list is not None:
        for password_salt in password_salt_list:
            saved_password = password_salt['password']
            saved_salt = password_salt['salt']
            if input_password == saved_password:
                messagebox.showinfo("Password validation", "Password validation successful!")
                return
    messagebox.showerror("Password validation", "Password validation failed!")

def open_webpage():
    webbrowser.open("https://ai.yucheng.life")