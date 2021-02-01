# P4 tk7

import tkinter as tk

def print_txtval():
    val_en = en.get()
    print(val_en)

root = tk.Tk()
root.title('get text box')
root.geometry('450x150')

lb = tk.Label(text = 'label')
en = tk.Entry()
bt = tk.Button(text='Button',command=print_txtval)
#[eidget.pack() for widget in [lb,en,bt]]
lb.pack()
en.pack()
bt.pack()
root.mainloop()

