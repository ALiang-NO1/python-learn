from tkinter import Tk, Label

root = Tk()
root.title('expand方法测试')
root.geometry('400x150-100+100')

Label(root, bg='gold', width=10).pack(side='left', fill='y')
Label(root, bg='orange', width=6, height=2).pack()
Label(root, bg='yellow').pack(fill='both', expand=True)

root.mainloop()