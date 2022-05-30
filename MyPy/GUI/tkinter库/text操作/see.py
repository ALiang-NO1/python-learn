import tkinter as tk
root=tk.Tk()
root.geometry('300x240')
b1=tk.Text(root,height=10,width=20)
b1.pack()

for i in range(1,20000):
    b1.insert(str(i)+".0",str(i)+"\n")
def see():
    b1.see('10000.0')

b2=tk.Button(root,text='See',command=see)
b2.pack()
root.mainloop()

"""
让index指定的字符在文本控件中可见。这个对于有很多文字内容的情况非常有用，可以让想看见的字符串立即可见，而不是使用滚动的方法。
"""