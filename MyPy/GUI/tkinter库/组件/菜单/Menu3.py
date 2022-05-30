from tkinter import *

def xianShi():
    # global root
    x1 = Label(root, text='I love China!!!', background='green', width=20, anchor='w')
    x1.pack()

root = Tk()   # 制作一个盛所有窗口的容器
root.geometry('400x100-100+100')

menubar = Menu(root)  # 制作一个菜单实例
for x in ['vb', 'c', 'java', 'php', 'c++']:
    menubar.add_command(label=x)

root['menu'] = menubar      # 注释看看
menubar.add_command(label='python', command=xianShi)
menubar.add_command(label='django', command=xianShi)

def pop(event):
    menubar.post(event.x_root, event.y_root)

root.bind('<Button-3>', pop)
root.mainloop()