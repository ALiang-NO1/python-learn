import tkinter as tk
root=tk.Tk()
root.geometry('300x240')
b1=tk.Text(root,height=10,width=20)
b1.pack()

def search():
    a=tk.IntVar()
    s=b1.search('1*','1.0',count=a,regexp=True)
    print(s,a.get())

b2=tk.Button(root,text='Search',command=search)
b2.pack()

root.mainloop()

"""
search( )
此方法的详细定义为search(pattern, index, stopindex=None,
forwards=None, backwards=None, exact=None,
regexp=None, nocase=None, count=None, elide=None)

查找字符串。这个方法比较复杂，参数比较多。下面一一介绍：
（1）pattern
定义要查找的内容。可以是字符串或者正则表达式。
（2）index
起始位置
（3）stopindex
结束位置。如果没有定义结束位置，会一直查找到末尾。如果stopindex的位置比index还要靠前，则返回空字符串。
（4）forwards
向前查找。(True 或者False)
（5）backwards
反向查找。(True 或者False)
（6）exact
是否精确匹配。(True 或者False)
（7）regexp
是否为正则表达式。(True 或者False)。
（8）nocase
是否区分大小写。默认是False，区分大小写。(True 或者False)
（9）count
匹配字符串的长度。需要设置IntVar变量来获取。这个选项对正则表达式的情况很有用。可以知道匹配正则的长度。如果没有使用正则，则返回的就是要寻找的字符串的长度。
（10）elide
"""