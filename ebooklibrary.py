import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')

def login():
    username = username_var.get()
    password = password_var.get()
    if username == "joespano" and password == "12345":
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
    else:
        messagebox.showerror(title="Error", message="Wrong, try again!")

frame = tk.Frame(bg='#333333')

# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_var = tk.StringVar()
username_entry = tk.Entry(frame, textvariable=username_var, font=("Arial", 16))
password_var = tk.StringVar()
password_entry = tk.Entry(frame, show="*", textvariable=password_var, font=("Arial", 16))
password_label = tk.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
