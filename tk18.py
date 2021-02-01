#tk18.pyw

import tkinter as tk
def print_txtval():
    val_en = en.get()
    print(val_en)

root = tk.Tk()
en = tk.Entry()
bt = tk.Button(text='Button',command=print_txtval)
[widget.pack() for widget in (en,bt)]
en.focus_set()

root.mainloop()