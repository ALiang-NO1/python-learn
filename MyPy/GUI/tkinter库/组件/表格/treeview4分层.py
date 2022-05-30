from tkinter import Tk
from tkinter.ttk import Treeview

root = Tk()
root.title('treeview测试')
root.geometry('400x150-100+100')

asia = {'中国': '北京', '日本': '东京', '泰国': '曼谷', '韩国': '首尔'}
euro = {'英国': '伦敦', '法国': '巴黎', '德国': '柏林', '挪威': '奥斯陆'}

tree = Treeview(root, columns='cities')
tree.heading('#0', text='国家')
tree.heading('#1', text='首都')

id_asia = tree.insert('', index='end', text='Asia')
id_euro = tree.insert('', index='end', text='Europe')

for country in asia.keys():
    tree.insert(id_asia, index='end', text=country, values=asia[country])
for country in euro.keys():
    tree.insert(id_euro, index='end', text=country, values=euro[country])
tree.pack()

root.mainloop()
