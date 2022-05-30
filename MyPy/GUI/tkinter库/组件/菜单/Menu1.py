from tkinter import *

root = Tk()
root.geometry('300x200-100+100')
root.wm_title('同济大学财务管理系统')
menubar = Menu(root)    # 指定菜单实例的父窗口是root
for item in ['文件', '编辑', '视图', '关于']:
    menubar.add_command(label=item)
root['menu'] = menubar    # 指定主窗口的'menu'属性为刚刚创建的menubar
root.mainloop()