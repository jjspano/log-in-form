import tkinter as tk
from tkinter import messagebox
import sqlite3

# Create a connection to the database
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create a table
c.execute('''CREATE TABLE IF NOT EXISTS users
             (id INTEGER PRIMARY KEY, username TEXT, password TEXT)''')
conn.commit()

class CustomLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg='#333333', fg="#FFFFFF", font=("Arial", 16))

class CustomEntry(tk.Entry):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(font=("Arial", 16))

class CustomButton(tk.Button):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.config(bg="#FF3399", fg="#FFFFFF", font=("Arial", 16))

def login():
    username = username_var.get()
    password = password_var.get()
    c.execute('SELECT * FROM users WHERE username=? AND password=?', (username, password))
    user = c.fetchone()
    if user:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

def register():
    username = username_var.get()
    password = password_var.get()
    c.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, password))
    conn.commit()
    messagebox.showinfo(title="Registration Success", message="User registered successfully.")

window = tk.Tk()
window.title("Login and Registration")
window.geometry('400x300')
window.configure(bg='#333333')

frame = tk.Frame(window, bg='#333333')

# Creating widgets
username_label = CustomLabel(frame, text="Username")
username_var = tk.StringVar()
username_entry = CustomEntry(frame, textvariable=username_var)
password_label = CustomLabel(frame, text="Password")
password_var = tk.StringVar()
password_entry = CustomEntry(frame, show="*", textvariable=password_var)
login_button = CustomButton(frame, text="Login", command=login)
register_button = CustomButton(frame, text="Register", command=register)

# Placing widgets on the screen
username_label.grid(row=0, column=0, pady=10)
username_entry.grid(row=0, column=1, padx=10, pady=10)
password_label.grid(row=1, column=0, pady=10)
password_entry.grid(row=1, column=1, padx=10, pady=10)
login_button.grid(row=2, column=0, columnspan=2, pady=10)
register_button.grid(row=3, column=0, columnspan=2, pady=10)

frame.pack(pady=30)

window.mainloop()

# Close the connection when done
conn.close()
