import tkinter as tk

root = tk.Tk()
root.geometry('180x130-100+100')

b1 = tk.Text(root, width=20, height=5)
b1.pack()

b3 = tk.Label(root, text='bbox:')
# 给出能够框住index代表的文字的4元组(x,y,width,height)。x,y是左上角的坐标点，而width和height分别是宽度和高度。
# 有了这些信息就可以判断诸如鼠标指针是否位于该index代表的文字范围内。
def bbox():
    b3['text'] = "bbox:" + str(b1.bbox('2.4'))

b2 = tk.Button(root, text='bbox', command=bbox)
b2.pack()
b3.pack()
root.mainloop()