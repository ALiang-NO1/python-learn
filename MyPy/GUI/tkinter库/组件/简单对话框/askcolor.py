from tkinter import *
from tkinter.colorchooser import askcolor

root = Tk(); root.geometry('400x150+400-300')

def test():
    s1 = askcolor(color='purple', title="选择背景色")
    print(s1)
    root.config(bg=s1[1])

Button(root, text="选择背景色", command=test).pack()

root.mainloop()