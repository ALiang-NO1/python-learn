"""测试listbox的添加、删除、排序功能、拖拽及滚动条的实现"""
from tkinter import Tk, Listbox, Entry, Button, BooleanVar, Checkbutton, Scrollbar

root = Tk()
root.title('listbox测试')
root.geometry('300x250-100+100')


def add_item():  # 插入输入框中的内容
    var_add = entry.get()
    if len(var_add.strip()) == 0:
        return
    box.insert('end', var_add)
    entry.delete(0, 'end')


def del_item():  # 删除选中的内容
    index = box.curselection()
    if len(index) == 0:
        return
    box.delete(index)  # 只能删一个


def sort():
    if var.get():
        tag = True
    else:
        tag = False
    lst = box.get(0, 'end')  # 获取所有行内容的元组
    sorted_lst = sorted(lst, reverse=tag)
    box.delete(0, 'end')
    for item in sorted_lst:
        box.insert('end', item)


def get_index(event):
    box.index = box.nearest(event.y)


def drag(event):
    new_index = box.nearest(event.y)
    if new_index < box.index:
        x = box.get(new_index)
        box.delete(new_index)
        box.insert(new_index + 1, x)
        box.index = new_index
    elif new_index > box.index:
        x = box.get(new_index)
        box.delete(new_index)
        box.insert(new_index - 1, x)
        box.index = new_index


entry = Entry(root)
entry.grid(row=0, column=0, padx=5, pady=5)
# 添加按钮
btn_add = Button(root, text='增加', width=10, command=add_item)
btn_add.grid(row=0, column=1, padx=5, pady=5, sticky='w')
# 列表盒子
box = Listbox(root)  # 高度是字符高
box.grid(row=1, column=0, padx=5, pady=5, sticky='w')
# 添加内容（水果）
fruits = ['Banana', 'Watermelon', 'Pineapple', 'Orange', 'Grapes', 'Mango']
for fruit in fruits:
    box.insert('end', fruit)
# 删除按钮
btn_del = Button(root, text='删除', width=10, command=del_item)
btn_del.grid(row=1, column=1, padx=5, pady=5, sticky='nw')
# 排序按钮
btn_sort = Button(root, text='排序', command=sort)
btn_sort.grid(row=1, column=1, padx=5, pady=50, sticky='nw')
# 排序复选框
var = BooleanVar()
cb = Checkbutton(root, text='降序', variable=var)
cb.grid(row=1, column=1, padx=50, pady=50, sticky='nw')
# 绑定拖拽函数
box.bind('<1>', get_index)
box.bind('<B1-Motion>', drag)
# 添加滚动条
scrollbar = Scrollbar(root)
scrollbar.grid(row=1, column=0, sticky='nse')
scrollbar.config(command=box.yview)

root.mainloop()
