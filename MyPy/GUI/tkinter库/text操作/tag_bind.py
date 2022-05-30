# 新绑定鼠标事件
import tkinter as tk

root = tk.Tk()
root.geometry('300x240')
b1 = tk.Text(root, height=10, width=20)
b1.pack()


def tag_mouse(*args):
    print('mouse click', *args)


def bind():
    b1.tag_add('mouse1', '1.0', '1.5')
    b1.tag_bind('mouse1', '<Button-1>', tag_mouse)


b2 = tk.Button(root, text='Tag_bind', command=bind)
b2.pack()
root.mainloop()

"""
tag_bind( tagName, sequence, func, add=None)
对tagName定义的文字区域绑定event。Event包括键盘输入、鼠标输入等。当有相应的输入的时候，定义的回调函数就会被触发。
（1）新建绑定事件
需要输入三个参数：tagName,sequence(需要绑定的事件)，func(回调函数)。tagName在这种情况下
（2）添加绑定事件
前面三个参数与（1）的相同。需要第四个参数：add=’+’。也就是说，同一个tag和同一个sequence，可以绑定多个回调函数。
（3）判断某个绑定事件是否存在
需要输入2个参数：tagName和sequence以及None。会返回指定tagName的sequence事件是否已经绑定。如果已经绑定，会返回相应回调函数。
（4）返回所有的绑定事件
只输入tagName以及None和None，就会会返回与此tagName有关的所有绑定事件。返回值是一个列表，包括所有的绑定的事件。不过绑定函数并没有返回。要知道确切的绑定事件，还需要再调用方法上面（3）的方法。
"""