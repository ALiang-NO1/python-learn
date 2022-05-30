from tkinter import Tk
from tkinter.ttk import Treeview

root = Tk()
root.title('测试treeview')
root.geometry('400x150-100+100')

def print_sel(event):
    widget = event.widget
    selected_item = widget.selection()[0]  # 获取行编号
    col = widget.item(selected_item, 'text')
    col2 = widget.item(selected_item, 'values')[0]  # 返回的是元组
    print('%s: %s' % (col, col2))

cities = {'加州': '洛杉矶', '德州': '休斯顿', '华盛顿': '西雅图', '江苏': '南京', '山东': '青岛', '广东': '广州', '福建': '厦门'}
tree = Treeview(root, columns='cities')
tree.heading('#0', text='State')
tree.heading('#1', text='City')

tree.column('#0', anchor='center')
tree.column('#1', anchor='center')
tree.tag_configure(tagname='evenColor', background='lightblue', foreground='pink')  # ??

rowCount = 1
for state in cities.keys():
    if rowCount % 2 == 1:
        tree.insert('', index='end', text=state, values=cities[state])
    else:
        tree.insert('', index='end', text=state, values=cities[state], tags='evenColor')
    rowCount += 1

tree.bind('<<TreeviewSelect>>', print_sel)
tree.pack()

root.mainloop()
