import tkinter as tk

root = tk.Tk()
root.geometry('300x200-100+100')
# font=('Courier New',10,)

def dlineinfo():
    b4['text'] = '结果:' + str(b1.dlineinfo(b3.get()))

b1 = tk.Text(root, width=25, height=8)
b1.pack()

b3 = tk.Entry(root)
b3.pack()

b2 = tk.Button(root, text='dlineinfo', command=dlineinfo)
b2.pack()

b4 = tk.Label(root, text='结果:')
b4.pack()

root.mainloop()
"""
》》返回由index指定的字符所在的行的信息，结果是一个5元组：
x:水平方向坐标，一般是2，因为文本与边框的距离默认值是2。
y:垂直方向坐标，一般是行数*(字符高度+行间距)+2*(文本与边框的默认距离)
width：字符宽度*每一行的字符总数
height: 字符高度+行间距
baseline: 与字符大小有关的一个结果
"""