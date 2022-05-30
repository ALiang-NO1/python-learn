import tkinter as tk
root=tk.Tk()
root.geometry('300x240')
b1=tk.Text(root,height=10,width=20)
b1.pack()
for i in range(1,5):
    b1.insert('1.0',str(i))

b1.mark_set('mark1','1.2')
b3=tk.Entry(root)
def mark_gravity():
    b1.mark_gravity('mark1',tk.LEFT)
    print(b1.mark_gravity('mark1'))
    print(b1.index('mark1'))
b2=tk.Button(root,text='Mark_gracity',command=mark_gravity)
b2.pack()
b3.pack()
root.mainloop()

"""
在markName指定的位置插入字符的时候，设置markName的位置是否变化。默认的方向是tk.RIGHT，markName的位置会始终在新插入字符的右侧，也就是会不断的变化。比如markName的位置在最开始是1.2，如果我们插入3个字符，那么mark Name的位置就是1.5。
如何保持markName的位置不变？设定方向为tk.LEFT就是可以了。这个时候markName的位置始终保持在设定的位置。所谓的不变化，指的是在markName指定的位置插入字符的时候。如果是在markName指定位置的前面，比如1.1的位置插入字符，markName的位置也会变化。
"""