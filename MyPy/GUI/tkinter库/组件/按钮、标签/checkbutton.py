from tkinter import *

myWindow = Tk()  # 创建一个tk窗口
myWindow.title('GUI程序练习')  # 窗口大标题
myWindow.geometry('260x60-100+100')  # 窗口位置及位置

check1 = Checkbutton(myWindow, text='Disabled', state='disable')
check1.select()  # select表示勾选，deselect表示不勾选
check1.grid(column=0, row=0, sticky=W)  # sticky表示左对齐


def func():
    if bool_var:
        print('复选框2被选中！')  # bool_var = True
    else:
        print('复选框2被取选！')
bool_var = BooleanVar()  # 字符串变量对象
print('bool_var:', bool_var.get())
check2 = Checkbutton(myWindow, text='UnChecked', variable=bool_var, highlightcolor='blue', highlightbackground='gold', state='active', command=func)
check2.setvar('value', 1)  # 给复选框设置一个变量
check2.setvar('value', 0)  # 覆盖原先的值
print('CheckButton2:', check2.getvar('value'))
check2.grid(column=1, row=0, sticky=W)

text_var = StringVar()
text_var.set('third')  # variable 覆盖 text
check3 = Checkbutton(myWindow, text='Enabled', textvariable=text_var, selectcolor='red', state='normal')
check3.grid(column=0, row=1, sticky=W)


def callcheckbutton():
    v.set('you have checked python!')
    check4['state'] = 'disable'

v = StringVar()
v.set('check python')
check4 = Checkbutton(myWindow, textvariable=v, disabledforeground='red', command=callcheckbutton)
check4.grid(column=1, row=1, sticky=W)

myWindow.mainloop()
