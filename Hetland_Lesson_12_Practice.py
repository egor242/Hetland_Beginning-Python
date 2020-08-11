from tkinter import *
from tkinter import messagebox as mb
from tkinter.scrolledtext import ScrolledText


def open_file():
    try:
        file_name = e.get()
        with open(file_name) as f:
            text.delete(1.0, END)
            file_contents = f.read()
            text.insert(1.0, file_contents)
    except FileNotFoundError:
        mb.showerror(title='Error', message='File does not exist')


def save_file():
    try:
        file_name = e.get()
        with open(file_name, 'w') as f:
            window_contents = text.get(1.0, END)
            f.write(window_contents)
            text.delete(1.0, END)
    except FileNotFoundError:
        mb.showerror(title='Error', message='File not chosen')


root = Tk()
root.title('Simple File Editor')

text = ScrolledText(width=65, height=30)
text.pack(side=BOTTOM, padx=7, pady=7, expand=True, fill=BOTH)

e = Entry(width=60)
e.pack(side=LEFT, padx=7, expand=True, fill=X)

open_button = Button(text='Open', command=open_file, width=9)
open_button.pack(side=RIGHT)

save_button = Button(text='Save', command=save_file, width=9)
save_button.pack(side=RIGHT, padx=7)


root.mainloop()