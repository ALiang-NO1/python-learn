import tkinter as tk

root = tk.Tk()
root.geometry('600x170-100+100')

def abc(*args):
    print(args)

def dump():
    b3['text'] = '结果:' + str(b1.dump('1.0', '4.0'))

b1 = tk.Text(root, width=60, height=5)
b1.pack()

b2 = tk.Button(root, text='Dump', command=dump)
b2.pack()

b3 = tk.Label(root, text='这里显示结果')
b3.pack()

root.mainloop()

"""
dump(index1, index2=None, command=None, kw)

返回标识index1和index2之间的内容。输入的参数为：
index1：起始标识
index2：结束标识。如果没有该参数，则只返回index1代表的字符信息。
command：用自定义函数处理返回的结果。在这种情况下，dump的返回结果是None。
**kw：定义返回何种类型的内容。可以选择的参数有：
all，image，mark，tag，text，window

返回的参数是一个三元组，包括（key，value，index）。
"""