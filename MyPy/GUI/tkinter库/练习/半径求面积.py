from tkinter import *

myWindow = Tk()  # 创建一个tk窗口
myWindow.title('GUI程序练习')  # 窗口大标题
myWindow.geometry('280x80-400+300')  # 窗口位置及位置


def printInfo():
    entry2.delete(0, END)
    R = int(entry1.get())
    s = 3.1415926 * R * R
    entry2.insert(8, s)
    entry1.delete(0, END)


Label(myWindow, text='intput').grid(row=0)
Label(myWindow, text='output').grid(row=1)
entry1 = Entry(myWindow)
entry2 = Entry(myWindow)
entry1.grid(row=0, column=1)
entry2.grid(row=1, column=1)
Button(myWindow, text='Quit', command=myWindow.quit).grid(row=2, column=0, sticky=W, padx=5, pady=5)
Button(myWindow, text='Run', command=printInfo).grid(row=2, column=1, sticky=W, padx=5, pady=5)

myWindow.mainloop()
