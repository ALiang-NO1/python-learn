import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag():
    b1.tag_add('second', '2.2', '2.5')
    print(b1.tag_prevrange('second', '2.4', '2.3'))


b2 = tk.Button(root, text='Tag', command=tag)
b2.pack()
root.mainloop()

"""
与tag_nextrange()非常类似。不过是反向搜索，也就是说是向前查找的。搜索的起始位置是index1前面的字符，然后到index2的位置截至。如果没有定义index2，会一直查找到文本控件的开始的地方。
需要注意的是，由于匹配还是从tagName代表的字符串的起始位置，所以index2的位置一定要小于或者等于tagName的起始位置，否则返回的是空字符串，哪怕tagName代表的字符串有部分位于[index2,index1]定义的区间。比如，tagName代表的是[‘2.2’,’2.5’]，那么index2一定要小于或者等于’2.2’。加入index2的值是’2.3’，返回就是空字符串。可以推测该方法的实现，是用tagName的起始位置和index2去比较，如果起始位置小于index2，就认为字符串不会被包含在[index2,index1]的区间内。
"""