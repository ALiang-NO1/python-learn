from tkinter import *

root = Tk()
root.title("测试Frame框架")
root.geometry('300x260-100+400')
f = Frame(root, width=280, height=250, cursor='cross', highlightcolor='gold', bg='green', bd=3, highlightthickness=5,
          relief='raised', takefocus=True)
f.pack()
root.mainloop()