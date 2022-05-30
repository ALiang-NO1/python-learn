from tkinter import *

root = Tk()
root.geometry('500x300-330+400')
root.title("测试布局管理place")
root['bg'] = 'seagreen'  # 海绿色的背景是root

f1 = Frame(root, width=200, height=200, bg='tan')  # 茶色的模块属于frame
f1.place(relx=0.2, rely=0.2)

Button(root, text="尚学堂").place(relx=0.2, rely=0.2, width=50, height=20)  # 在root中的相对位置
Button(f1, text="晾").place(relx=0.8, rely=0.8)  # 相对frame的位置
Button(f1, text="瑞").place(relx=0.3, rely=0.3, relwidth=0.5, relheight=0.6)

root.mainloop()
