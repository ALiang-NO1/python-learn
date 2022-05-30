from tkinter import *

root = Tk()
root.geometry('200x100-200+270')

v = StringVar()
v.set("西瓜")
# 方法一
om = OptionMenu(root, v, "冬瓜", "南瓜", "西瓜", "哈密瓜")
# 方法二
# melons = ('', '', '')
# om = OptionMenu(root, v, *melons)

om['width'] = 10
om.pack()

def test():
    print("最爱的瓜：", v.get())

Button(root, text='确定', command=test).pack()

root.mainloop()