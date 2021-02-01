import thinter as tk
root = tk.Tk()
root.title('Widget creation')
root.geometry('450x450')
lb = tk.Label(text='Label-1')
bt = tk.Button(text='BUTTON-1')
lb.pack()
bt.pack()
root.mainloop()