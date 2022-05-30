# 添加绑定事件，判断某个事件是否存在以及返回所有绑定事件
# 新绑定鼠标事件
import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag_mouse(*args):
    print('mouse click', *args)


def ctrl(*args):
    print('Control_Left', *args)


def add():
    b1.tag_bind('mouse1', '<Control_L>', ctrl)


def bind():
    b1.tag_add('mouse1', '1.0', '1.5')
    b1.tag_bind('mouse1', '<Button-1>', tag_mouse)


def list_events():
    print(b1.tag_bind('mouse1', None, None))


def list_func():
    print(b1.tag_bind('mouse1', '<Button-1>', None))
    print(b1.tag_bind('mouse1', '<Control_L>', None))


b2 = tk.Button(root, text='Tag_bind', command=bind)
b2.pack()
b3 = tk.Button(root, text='Add_Event', command=add)
b3.pack()
b4 = tk.Button(root, text='List_Events', command=list_events)
b4.pack()
b5 = tk.Button(root, text='Liset_Func', command=list_func)
b5.pack()
root.mainloop()