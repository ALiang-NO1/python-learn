from tkinter import *
from tkinter.ttk import Separator

myWindow = Tk()    # 创建一个tk窗口
myWindow.title('GUI程序练习')    # 窗口大标题
myWindow.geometry('250x300-100+100')    # 窗口位置及位置

language = [('python', 0), ('c++', 1), ('c', 2), ('java', 3)]
v = IntVar()

label = Label(myWindow, text='empty', bg='yellow')
label.pack(anchor='w')
Label(myWindow, text='选择一们你喜欢的编程语言').pack(anchor='w')

def callback():
    if v.get() in range(4):
        label.config(text="你选择的是：" + language[v.get()][0])
        root = Tk()
        root.geometry('200x100+500+100')
        Label(root, text='你选择的是'+language[v.get()][0], fg='red', width=20, height=3).pack()
        Button(root, text='确定', width=3, height=1, command=root.destroy).pack(side='bottom')

for lan, num in language:
    Radiobutton(myWindow, text=lan, value=num, command=callback, variable=v).pack(anchor='w')

Separator(myWindow).pack(pady=2, fill='x')

var = StringVar()
cities = {0: '纽约', 1: '东京', 2: '巴黎', 3: '伦敦'}
for val, city in cities.items():
    Radiobutton(myWindow, text=city, value=val, width=20, indicatoron=0).pack(pady=2, anchor='w')

myWindow.mainloop()