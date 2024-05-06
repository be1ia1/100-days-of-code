import tkinter

def button_clicked():
    user_input = input.get()
    label['text'] = f'I got clicked: {user_input}'

window = tkinter.Tk()

window.title('My GUI Program')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

label = tkinter.Label(text='I am a Label', font=('Arial', 24))
label['text'] = 'New Text'
label.grid(column=0, row=0)



button = tkinter.Button(text='Click Me', command=button_clicked)
button.grid(column=1, row=1)

button2 = tkinter.Button(text='Click Me', command=button_clicked)
button2.grid(column=3, row=0)

input = tkinter.Entry(width=10)
input.grid(column=4, row=2)


window.mainloop()
    