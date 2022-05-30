import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.geometry('350x240-100+100')

tk.Label(root, text='成绩表').grid(row=0)

area = ('姓名', '数学', '语文', '英语')
ac = ('name', 'math', 'chinese', 'english')
data = [('张三', '90', '88', '95'), 
      ('李四', '100', '92',  '90'), 
      ('王二', '88', '90',  '91')]
tv = ttk.Treeview(root, columns=ac, show='headings', height=5, padding=(2, 10, 10, 10))

for i in range(4):
    tv.column(ac[i], width=70, anchor='center')
    tv.heading(ac[i], text=area[i])     # 设置标题，有分割线
tv.grid(row=1, columnspan=4)
for i in range(3):
    for j in range(3):
        tv.insert('', 'end', values=data[i])
def select(*args):
    print(tv.selection())
    # print('选择的行：', tv.bbox(tv.selection()))      # 选中行的框选范围（左上角坐标，width, height）
    # print('第三列：', tv.bbox(tv.selection(), column='chinese'))    # 选中行的第三个单元格的框选范围。
tv.bind('<<TreeviewSelect>>', select)

print('tv.column3:', tv.column(3))

def column():
    tv.column(2, width=50)
ttk.Button(root, text='Column', command=column).grid(row=2, column=0)

def delete():
    tv.delete(tv.selection())
ttk.Button(root, text='Delete', command=delete).grid(row=2, column=1)

detach = None
index = None
def detach():
    global detach
    global index
    detach = tv.selection()
    index = tv.index(detach)
    tv.detach(detach)
def attach():
    global detach
    global index
    if detach:
        tv.move(detach, '', index)
ttk.Button(root, text='Detach', command=detach).grid(row=2, column=2)
ttk.Button(root, text='Attach', command=attach).grid(row=2, column=3)

print('exists I002:', tv.exists('I002'))

def focus():
    print(tv.focus())
ttk.Button(root, text='Focus', command=focus).grid(row=3, column=0)

def heading():
    print(tv.heading(column=1))
ttk.Button(root, text='Heading', command=heading).grid(row=3, column=1)

def identify():
    print(tv.identify('region', 120, 30))
ttk.Button(root, text='Identify', command=identify).grid(row=3, column=2)

def selection():
    tv.selection_set('I001', 'I002')
ttk.Button(root, text='Selection', command=selection).grid(row=3, column=3)

root.mainloop()