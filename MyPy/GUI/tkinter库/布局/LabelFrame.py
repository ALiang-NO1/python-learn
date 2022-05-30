from tkinter import Tk, LabelFrame, BooleanVar, Button, Checkbutton

root = Tk()
root.title('LabelFrame测试')
root.geometry('200x200-100+100')

lf = LabelFrame(root, text='你喜欢的球类', bg='beige', fg='blue')  # 单位像素
sports = {0: '篮球', 1: '棒球', 2: '足球', 3: '网球'}
checkboxes = {}
for i in range(len(sports)):
    checkboxes[i] = BooleanVar()
    Checkbutton(lf, text=sports[i], variable=checkboxes[i]).grid(row=i+1, sticky='w')
lf.pack(ipadx=5, ipady=5, pady=10)

def printInfo():
    selection = ''
    for i in checkboxes:
        if checkboxes[i].get() == True:
            selection += sports[i] + '\t'
    print(selection)

btn = Button(root, text='确定', width=10, command=printInfo).pack()

root.mainloop()
