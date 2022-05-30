import tkinter as tk

root = tk.Tk()
root.geometry('300x200-100+100')
b1 = tk.Text(root, width=30, height=12)
b1.pack()

def delete():
    b1.delete(1.1, 2.3)

b2 = tk.Button(root, text='Delete', command=delete)
b2.pack()
root.mainloop()