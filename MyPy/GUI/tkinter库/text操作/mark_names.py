import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()
b3 = tk.Entry(root)
b4 = tk.Entry(root)


def mark_set():
    b1.mark_set(b3.get(), b4.get())
    print(b1.mark_names())
    print(b1.index('mark1'))


b2 = tk.Button(root, text='Mark_set', command=mark_set)
b2.pack()
b3.pack()
b4.pack()
root.mainloop()

"""
返回所有的位置标识(mark)的名称，包括tk.INSERT,tk.CURRENT和’tk::anchor1’。一般情况下，’tk::anchor1’指向最后一行的最后一个字符之后的位置，也就是最后一行的行尾。
10.3.23 mark_set(markName, index)
在index指定的位置之前设定一个位置标识(mark)，用markName来标识。该位置标识(mark)的gravity默认值是tk.RIGHT。
可以在同一个index处设置不同名字的位置标识（mark）。如果在不同的index处设置同样名字的位置标识(mark)，只会记录最新的index。

import tkinter as tk
"""