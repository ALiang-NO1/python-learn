from tkinter import Tk, Entry, Label, StringVar, Button

root = Tk()
root.title('简单计算机')
root.geometry('250x120-100+100')

formula = StringVar()
def callbackW(*args): print('changed data:', formula.get())
formula.trace('w', callbackW)
def callbackR(*args): print('数据被读取！')
formula.trace('r', callbackR)

inp = Entry(root, textvariable=formula, highlightbackground='gold', highlightcolor='green',
            selectbackground='lightblue', selectborderwidth=2, selectforeground='red',
            exportselection=True, xscrollcommand=True)
inp.pack()

def cal():
    if res:
        res.set('结果是：' + str(eval(formula.get())))
        formula.set('')
Button(root, text='运算', command=cal).pack()

res = StringVar()
Label(root, textvariable=res, bg='gold', font='黑体 18').pack()

root.mainloop()