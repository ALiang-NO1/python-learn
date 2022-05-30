from tkinter import *

myWindow = Tk()    # 创建一个tk窗口
myWindow.title('GUI程序练习')    # 窗口大标题
myWindow.geometry('650x160+500-100')    # 窗口位置及位置

b1 = Button(myWindow, text='按钮1', bg='silver', fg='green', relief='raised', cursor='plus', width=14, height=3,
            bd=3, takefocus=False, overrelief='groove', activebackground='gold')
b1.grid(row=0, column=0, sticky=E, padx=5, pady=5)

p = PhotoImage(file='../pic.gif')
b2 = Button(myWindow, text='按钮2', font='Helvetica 10 bold', image=p, compound='bottom',
            cursor='circle', relief='solid', activebackground='coral')
b2.grid(row=0, column=1)

b3 = Button(myWindow, text='按钮3我OA的看法克拉斯', relief='groove', activebackground='blue', width=9, height=3,
            overrelief='flat', takefocus=True, wraplength=50, activeforeground='red',)
b3.grid(row=0, column=2, padx=5)

myWindow.resizable(width=True, height=True)    # 设置宽高是否可变(0,0)
myWindow.mainloop()    # 事件循环