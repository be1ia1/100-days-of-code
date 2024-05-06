import tkinter as tk

def calc_km():
    miles = int(user_input.get())
    kilometers = miles * 1.6
    label2_km.config(text=kilometers)

window = tk.Tk()
window.minsize(width=280, height=100)
window.config(padx=10, pady=10)

user_input = tk.Entry()
user_input.grid(column=1, row=0)

label_miles = tk.Label()
label_miles.config(text='Miles')
label_miles.grid(column=3, row=0)

label1_km = tk.Label()
label1_km.config(text='is equal to')
label1_km.grid(column=0, row=1)

label2_km = tk.Label()
label2_km.config(text=0)
label2_km.grid(column=1, row=1)

label3_km = tk.Label()
label3_km.config(text='Km')
label3_km.grid(column=2, row=1)

button = tk.Button()
button.config(text='Calculate', command=calc_km)
button.grid(column=1, row=2)

window.mainloop()