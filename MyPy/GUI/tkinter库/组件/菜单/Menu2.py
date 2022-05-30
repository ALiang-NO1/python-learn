from tkinter import *

root = Tk()
root.geometry('300x200-100+100')

def show_menu(event):
    fmenu.post(event.x_root, event.y_root)

menubar = Menu(root)    # it produces a menu instance
fmenu = Menu(menubar, tearoff=0)  # 没有虚线，不可拆分
for item in {'新建': 'Ctr+o', '打开': 'Ctr+n', '保存': 'save', '另存为': 'save+as'}.items():
    fmenu.add_cascade(label=item[0], accelerator=item[1], underline=0)  # 添加快捷键说明
emenu = Menu(menubar)
for item in ['复制', '粘贴', '剪切']:
    emenu.add_cascade(label=item)
vmenu = Menu(menubar)
for item in ['默认视图', '新式视图']:
    vmenu.add_cascade(label=item)
amenu = Menu(menubar)
for item in ['版权信息', '其他说明']:
    amenu.add_cascade(label=item)
menubar.add_cascade(label='文件', menu=fmenu)
menubar.add_cascade(label='编辑', menu=emenu)
menubar.add_cascade(label='视图', menu=vmenu)
menubar.add_cascade(label='关于', menu=amenu)

root['menu'] = menubar
root.mainloop()