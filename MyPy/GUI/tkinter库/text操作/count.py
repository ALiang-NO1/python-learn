import tkinter as tk

root = tk.Tk()
root.geometry('300x200-100+100')

def count():
    label['text'] = '结果:' + str(text.count(1.1, 2.5, 'update'))

text = tk.Text(root, width=20, height=5)
text.pack()

button = tk.Button(root, text='Count', command=count)
button.pack()

label = tk.Label(root, text='结果:')
label.pack()

entry = tk.Entry(root)
entry.pack()

root.mainloop()

"""
count(index1, index2, args)
count方法是新增的。主要的功能是统计在标识index1与index2之间的有关数据。统计什么数据是由*args参数来决定的。包括：
（1）chars: 统计字符数。主要如果跨行，换行符也统计在内。
（2）displaychars：显示的字符数
（3）displayindices：显示的索引数
（4）displaylines：显示的行数，在有折行的情况下，会比lines增多。因为折行也被计算为行数。
（5）indices：索引数
（6）lines：行数（从0开始计数）
（7）xpixels: 水平方向上index1和index2之间的像素差
（8）ypixels：垂直方向上index1和index2之间的像素差
（9）update：更新。避免出现统计误差。
"""