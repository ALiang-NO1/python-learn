import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag():
    b1.tag_add('second', '2.2', '2.5')
    print(b1.tag_nextrange('second', '2.0', '2.3'))


b2 = tk.Button(root, text='Tag', command=tag)
b2.pack()

root.mainloop()

"""
搜索tagName是否在index1和index2定义的区域内。如果没有定义index2，则表示到文本控件的结尾。
如果tagName在该区域内，则返回tagName表示的[‘首字符’,’尾字符’]。如果tagName不在指定的区域，则返回空字符串。
只要有部分tagName代表的字符落在[index1,index2]的区域内，就满足搜索条件，返回tagName代表的首字符和尾字符。
"""