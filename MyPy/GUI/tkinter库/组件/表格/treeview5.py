from tkinter import Tk
from tkinter.ttk import Treeview, Style
from PIL import ImageTk, Image

root = Tk()
root.title('treeview测试')
root.geometry('420x220-100+100')

Style().configure('Treeview', rowheight=50)
info = ['我国最长的桥是武汉长江大桥（瞎编的）', '我国最靓的仔——周杰伦', '哀悼袁荣平去世。。。']

tree = Treeview(root, columns='说明')
tree.heading('#0', text='消息来源')
tree.heading('#1', text='详细信息')
tree.column('#1', width=300)

file = Image.open(r'..\logo.png')
img = ImageTk.PhotoImage(file)
origin = ['凤凰新闻', '腾讯新闻', '搜狗头条']
for i in range(len(origin)):
    tree.insert('', index='end', text=origin[i], image=img, values=info[i])

tree.pack()

root.mainloop()
