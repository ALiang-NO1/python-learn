"""测试树视图设置标题栏，添加、插入、删除内容，设置栏属性，设置双击事件"""
from tkinter import Tk, Button, Entry
from tkinter.ttk import Treeview

root = Tk()
root.title('Treeview测试')
root.geometry('350x250-100+100')
# 行随窗口缩放比例 1:1
root.rowconfigure(1, weight=1)
root.columnconfigure(1, weight=1)
root.columnconfigure(3, weight=1)

def remove():
    iids = tree.selection()
    for iid in iids:
        tree.delete(iid)
    print('已经删除行：', iids)

def insert():
    state = entry1.get()
    city = entry2.get()
    if len(state.strip()) == 0 or len((city.strip())) == 0:
        return
    tree.insert('', 'end', text=state, values=city)
    entry1.delete(0, 'end')
    entry2.delete(0, 'end')

def diclick(event):
    e = event.widget
    iid = e.identify('item', event.x, event.y)
    state = e.item(iid, 'text')
    values = e.item(iid, 'values')
    print('Double clicked: '+state, end='\t')
    for v in values:
        print(v, end='\t')
    print()

def sort_tree(col):
    global reverse_flag
    # print(tree.get_children(''))  # 获取所有行的id
    lst = [(tree.set(st, col), st) for st in tree.get_children('')]  # -> 迭代器（set，行id）
    lst.sort(reverse=reverse_flag)
    for index, item in enumerate(lst):
        tree.move(item[1], '', index)
    reverse_flag = not reverse_flag

reverse_flag = False
entry1 = Entry(root)
entry2 = Entry(root)
entry1.pack(padx=5, pady=3, anchor='w')
entry2.pack(padx=5, anchor='w')

tree = Treeview(root, columns=('cities', 'populations'), selectmode='extended')  # 设置三栏：图标、城市、人口数，无图标栏：show='headings'
# 建立栏标题
tree.heading('#0', text='State', command=lambda c='cities': sort_tree(c))  # 图标栏
# tree.heading('cities', text='City')
tree.heading('#1', text='City')
tree.heading('#2', text='Populations')
# 设置栏位格式
tree.column('#0', anchor='center', width=80)
tree.column('#1', anchor='center', width=80)
tree.column('#2', anchor='center', width=100)
# 建立内容
tree.insert('', index='end', text='长春', values=('长大', 20000))
tree.insert('', index='end', text='西安', values='西大')  # 父id 插入位置 图标栏内容 值
tree.pack(side='left', padx=5, pady=3, anchor='nw')
# 列出列属性
# city_dict = tree.column('cities')
# print(city_dict)

Button(root, text='删除', command=remove).pack(anchor='nw', padx=5, pady=3)
Button(root, text='插入', command=insert).pack(anchor='nw', padx=5, pady=3)
tree.bind('<Double-1>', diclick)

root.mainloop()
