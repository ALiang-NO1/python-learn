from tkinter import *

root = Tk()
m = Menu(root)    # 创建一个菜单实例m, 这个菜单实例依附在主窗口root上面。

m2 = Menu(m)    # 创建一个二级菜单实例，这个实例依附在菜单m上，因为Menu的参数是widget, 它是一个窗口, m也算是一个窗口了，只不过是菜单窗口。
for item in ['python', 'perl', 'php', 'ruby']:
    m2.add_command(label=item)    # 菜单m2调用add_command方法，用来增加菜单项目标签

m2.add_separator()    # 添加分割线，不需要任何参数
for item in ['java', 'c++', 'c']:
    m2.add_command(label=item)    # 增加二级菜单项目标签

m.add_cascade(label='语言', menu=m2)    # 给依附在root容器上的一级菜单m增加一个二级菜单
root['menu'] = m    # 给root增加菜单属性，让其拥有一级菜单
root.mainloop()