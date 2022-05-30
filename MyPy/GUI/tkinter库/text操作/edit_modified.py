import tkinter as tk

root = tk.Tk()
root.geometry('300x200-100+100')

b1 = tk.Text(root, width=25, height=10, )
b1.pack()

def edit_modified():
    print(b1.edit_modified())
    
b2 = tk.Button(root, text='edit_modified', command=edit_modified)
b2.pack()

root.mainloop()