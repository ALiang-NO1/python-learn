from tkinter import *

root = Tk(); root.geometry('200x180-150-200')
c1 = Canvas(width=200, height=150, bg='salmon'); c1.pack()

def mouseTest(event):
    print("鼠标左键单击位置（相对于父容器）：({0}, {1})".format(event.x, event.y))
    print("鼠标左键单击位置（相对于屏幕）：({0}, {1})".format(event.x_root, event.y_root))
    print("事件绑定的组件：{0}".format(event.widget))

def testDrag(event):
    i = 40
    c1.create_oval(event.x, event.y, event.x+i, event.y+i)

def keyboardTest(event):
    print("按下键！编码(keycode):{0}|字符(char):{1}|名称(keysym):{2}".format(event.keycode, event.char, event.keysym))

def press_a_test(event):
    print('press a')

def release_a_test(event):
    print('release a')

c1.bind('<1>', mouseTest)
c1.bind('<B1-Motion>', testDrag)
root.bind('<KeyPress>', keyboardTest)
root.bind('<KeyPress-a>', press_a_test)
root.bind('<KeyRelease-a>', release_a_test)

def mouseTest1(event):
    print("bind方式绑定，可以获取event对象:", event.widget)
    print("widget名：", event.widget)

def mouseTest2():
    print("通过command方式绑定，不能直接获取event对象")

def mouseTest3(event):
    print("右键单击事件，绑定给所有按钮了！enent对象：", event.widget)

# bind绑定事件
b1 = Button(root, text="bind")
b1.pack(side='left')
b1.bind('<Button-1>', mouseTest1)

# command属性直接绑定事件
b2 = Button(root, text='click', command=lambda: mouseTest2())
b2.bind('<Button-3>', mouseTest3)
b2.pack(side='left')

root.mainloop()