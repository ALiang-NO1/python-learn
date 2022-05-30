from tkinter import *

root = Tk(); root.geometry('240x50-300+200')

def mouseTest1():
    print("command方式，简单情况（不涉及event对象），可以使用")

def mouseTest2(e):
    print(e.char)

Button(root, text="测试command1", command=mouseTest2).pack(side='left')
Button(root, text="测试command2", command=lambda e: print(e.char)).pack(side='left')

root.mainloop()