"""文件对话框获取文档"""

from tkinter.filedialog import *

root = Tk(); root.geometry('600x100-100+100')

def test():
    f = askopenfile(title="打开文件", initialdir=r'E:\PDF文档', filetype=[("pdf文档", ".pdf")])
    show['text'] = f
    print(f)
    print(f.name)
    print(f.encoding)

Button(root, text="选择编辑的文件", command=test).pack()
show = Label(root, width=80, height=2, bg='beige', font='黑体 9')
show.pack()

root.mainloop()