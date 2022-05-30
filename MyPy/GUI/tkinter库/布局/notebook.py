"""测试notebook"""
from tkinter import Tk, Frame, Label, Button, messagebox, PhotoImage
from tkinter.ttk import Notebook

root = Tk()
root.title('测试notebook')
root.geometry('400x150-100+100')

notebook = Notebook(root)

def msg():
    messagebox.showinfo('Notebook', '欢迎使用Notebook')

frame1 = Frame()
frame2 = Frame()
# 框架1放置标签
label = Label(frame1, text='HTML')
label.pack(padx=10, pady=10)
# 框架2放置按钮
btn = Button(frame2, text='Help', command=msg)
btn.pack(padx=10, pady=10)

notebook.add(frame1, text='选项卡1')
notebook.add(frame2, text='选项卡2')
notebook.pack(padx=10, pady=10, fill='both', expand=True)

root.mainloop()