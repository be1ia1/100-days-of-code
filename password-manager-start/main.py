import pyperclip
import pandas as pd
import json
from random import randint, choice, shuffle
import tkinter as tk
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list.extend([choice(letters) for _ in range(randint(8, 10))])
    password_list.extend([choice(symbols) for _ in range(randint(2, 4))])
    password_list.extend([choice(numbers) for _ in range(randint(2, 4))])
    shuffle(password_list)
    password = ''.join(password_list)

    pyperclip.copy(password)
    entry_password.insert(0, password)
    

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    site = entry_website.get()
    email = entry_email.get()
    password = entry_password.get()
    is_not_empty = all([site, email, password])
    if is_not_empty:
        is_ok = messagebox.askokcancel(title=site,
                            message=f'These are the details entered:\n \
                            Email: {email}\nPassword: {password}\n \
                                Is it ok to save?')
        if is_ok:
            new_data = {
                site : {
                    "username": email,
                    "password": password
                }
            }
            with open('database.json', encoding="utf8") as fo:
                data = json.load(fo)
            with open('database.json', "w", encoding="utf8") as fo:
                if data:
                    data.update(new_data)
                    json.dump(data, fo, indent=4)
                else:
                    json.dump(new_data, fo, indent=4)
            entry_website.delete(0, tk.END)
            entry_password.delete(0, tk.END)
    else:
        messagebox.showwarning(title='Oops..', message='Check empty fields..')
# ---------------------------- GET PASSWORD -------------------------- #
def get_password():
    with open('database.json', encoding="utf8") as fo:
        data = json.load(fo)
    u_site = entry_website.get()
    if u_site in data.keys():
        u_password = data[u_site]['password']
        pyperclip.copy(u_password)
        entry_password.insert(0, u_password)


# ---------------------------- UI SETUP ------------------------------- #

window = tk.Tk()
window.title('Password Manager')
window.config(padx=50, pady=50)

canvas = tk.Canvas(width=200, height=200)
photo = tk.PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=photo)
canvas.grid(column=1,row=0)

label_website = tk.Label(text='Website:')
label_website.grid(column=0, row=1)

entry_website = tk.Entry(width=35)
entry_website.grid(column=1, row=1, sticky=tk.EW)
entry_website.focus()

button_search = tk.Button(text='Search', command=get_password)
button_search.grid(column=2, row=1, sticky=tk.EW)

label_email = tk.Label(text='Email/Username:')
label_email.grid(column=0, row=2)

entry_email = tk.Entry(width=35)
entry_email.grid(column=1, row=2, columnspan=2, sticky=tk.EW)
entry_email.insert(0, 'belial.ahula@gmail.com')

label_password = tk.Label(text='Password:')
label_password.grid(column=0, row=3)

entry_password = tk.Entry(width=21)
entry_password.grid(column=1, row=3, sticky=tk.EW)

button_password = tk.Button(text='Generate Password', command=generate_password)
button_password.grid(column=2, row=3)

button_add = tk.Button(text='Add', width=36, command=save_password)
button_add.grid(column=1, row=4, columnspan=2, sticky=tk.EW)


window.mainloop()