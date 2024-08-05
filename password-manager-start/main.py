import tkinter as tk
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    pass
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
            with open('database.txt', 'a') as fo:
                fo.write(f'{site} | {email} | {password}\n')
            entry_website.delete(0, tk.END)
            entry_password.delete(0, tk.END)
    else:
        messagebox.showwarning(title='Oops..', message='Check empty fields..')
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
entry_website.grid(column=1, row=1, columnspan=2, sticky=tk.EW)
entry_website.focus()

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