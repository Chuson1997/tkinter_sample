#tk13.pyw
import tkinter as tk

root = tk.Tk()
root.geometry('300x200')
lb = tk.Label(text='This is a Label, This is a Label, This is a Label')
ms = tk.Message(text='This is a Message. This is a Message. This is a Message')
[widget.pack() for widget in (lb,ms)]
root.mainloop()