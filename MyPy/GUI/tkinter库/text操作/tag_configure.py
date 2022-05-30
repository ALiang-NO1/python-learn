import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag():
    b1.tag_add('second', '2.0', '2.10')
    b1.tag_configure('second', background='red')


b2 = tk.Button(root, text='Tag', command=tag)
b2.pack()
root.mainloop()

# 底纹代码
import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag():
    b1.tag_add('second', '2.0', '2.10')
    b1.tag_configure('second', background='red', bgstipple='gray12')


b2 = tk.Button(root, text='Tag', command=tag)
b2.pack()
root.mainloop()

# 底纹代码
import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag():
    b1.tag_add('second', '2.0', '2.10')
    b1.tag_configure('second', background='red', bgstipple='gray12')


b2 = tk.Button(root, text='Tag', command=tag)
b2.pack()
root.mainloop()