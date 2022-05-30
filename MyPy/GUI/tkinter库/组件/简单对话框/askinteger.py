from tkinter.simpledialog import *

root = Tk(); root.geometry('400x150+400-280')

def test():
    a = askinteger(title="请输入年龄", prompt='')
    show['text'] = a

Button(root, text="你年龄多大了，请输入！", command=test).pack()
show = Label(root, width='40', height=3, bg='silver')
show.pack()

root.mainloop()