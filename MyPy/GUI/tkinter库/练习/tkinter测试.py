from tkinter import *
from tkinter import messagebox

root = Tk('GUI程序测试')
root.geometry('400x440-100+100')

intvar = IntVar()
cek_bt = Checkbutton(root, text='test', variable=intvar)
cek_bt.pack()
btn = Button(root, text='button')
btn.pack()
def check(e):
    print(cek_bt.getvar())
btn.bind('<1>', check)

root.mainloop()

