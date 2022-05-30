import tkinter as tk
root=tk.Tk()
root.geometry('300x240')
b1=tk.Text(root,height=10,width=20)
b1.pack()
b3=tk.Label(b1,text='abc')
for i in range(1,11):
    b1.insert('1.0',str(i))

def win():
    b1.window_create('1.2',window=b3)
    print(b1.window_names())
b2=tk.Button(root,text='Window Create',command=win)
b2.pack()
root.mainloop()

"""
返回值为：(<textindex object: ‘2.2’>, <textindex object: ‘2.5’>, <textindex object: ‘3.2’>, <textindex object: ‘3.3’>)

10.3.42 tag_remove( tagName, index1, index2=None)
从tagName中移除在区间[index1,index2]之间的字符。如果没有定义index2，则只移除index1代表的单个字符。如果[index1,index2]是在tagName的中间，则会分割tagName代表的字符串为2个。
比如，tagName的起始区间是[‘2.2’,’2.8’]，如果index1和index2分别是’2.3’和’2.5’，调用tag_remove之后，tagName的区间变为[‘2.2’,’2.3’]以及[‘2.5’,’2.8’]。也就是tagName代表的区间一分为二。
这里的移除字符，不是从文本控件中删除字符，而是从tagName代表的区间中去掉字符。
**10.3.43 window_create(index, cnf={}, kw)
创建窗口的用处是在文本控件中指定的位置创建嵌入式对象。比如，创建一个标签(Label)、输入框(Entry)等等。
创建嵌入式对象的方法有两种：
（1）先创建文本对象的子控件，但是不要使用pack或者grid让该子控件显示。而是作为一个参数，传递给window_create方法。比如下面代码中的：
b3=tk.Label(b1,text=‘abc’)
b1.window_create(‘1.2’,window=b3)

（2）第二种方法是通过-create参数传递一个回调函数。在回调函数中创建文本控件的子控件。
"""