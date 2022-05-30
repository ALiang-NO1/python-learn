"""测试文本框属性，更改、调整字体样式、大小、粗细，获取、修改和删除内容"""
from tkinter import Tk, Scrollbar, Text, Frame, StringVar, OptionMenu, Button, TclError, SEL_FIRST, SEL_LAST
from tkinter.ttk import Combobox
from tkinter.font import Font

root = Tk()
root.title('测试文本框')
root.geometry('-100+100')

def change_family(event):  # 改变字体
    f = Font(family=var_family.get())
    text['font'] = f

def change_weight(event):  # 改变粗细
    w = Font(weight=var_weight.get())
    text['font'] = w

def change_size(event):  # 改变大小
    s = Font(size=var_size.get())
    text['font'] = s

def print_sel():  # 打印选中内容
    try:
        select_text = text.get(SEL_FIRST, SEL_LAST)  # 删除：delete(0, 'end')
        print('选取文字：', select_text)
    except TclError:
        print('未选中文字！')

def print_index():
    print('insert:', text.index('insert'))
    print('current:', text.index('current'))
    print('end:', text.index('end'))

frame = Frame(root, bg='lightgreen')
frame.pack(side='left', padx=5, pady=5, anchor='nw')

# 文本框
text = Text(frame, width=30, height=9, font='楷体 16', fg='blue', undo=True)
text.pack(side='left')
text.insert('end', 'So much for today,let`s begin tomorrow!\n')
for i in range(5):
    text.insert('end', '成功没有捷径，努力是必要条件！\n')
# 为文本框添加标记
text.mark_set('mark1', 1.0)  # 标记的是文本（字符）间的空白，从第一行开始，列从左边空白算起，最小索引为0
text.mark_set('mark2', 4.1)
print('mark:', text.get('mark1', 'mark2'))  # 返回标记间夹的文本
# 为索引间的文本添加标签
text.tag_add('tag1', 1.12, 1.17)
text.tag_add('tag2', 3.7, 3.16)
text.tag_config('tag1', justify='center', underline=True, foreground='red')  # 设置标记1样式
text.tag_config('tag2', justify='right', overstrike=True, foreground='red')  # 设置标记1样式
# 删除索引间内容
text.delete(6.7, 6.16)

# 建立垂直滚动条
scrollbar = Scrollbar(frame)
scrollbar.pack(fill='y', side='left')
scrollbar.config(command=text.yview)
text.config(yscrollcommand=scrollbar.set)
text.focus_set()

# 字体
var_family = StringVar()
font_family = ('Arial', 'Times', 'Courier')
var_family.set(font_family[0])
family = OptionMenu(root, var_family, *font_family, command=change_family)
family.pack(anchor='nw')
# 字体粗细
var_weight = StringVar()
font_weight = ('normal', 'bold')
var_weight.set(font_weight[0])
weight = OptionMenu(root, var_weight, *font_weight, command=change_weight)
weight.pack(anchor='nw', pady=3)
# 字体大小
var_size = StringVar()
font_sizes = [x for x in range(8, 30)]
size = Combobox(root, textvariable=var_size, value=font_sizes)
size.current(8)
size.bind('<<ComboboxSelected>>', change_size)
size.bind('<Return>', change_size)
size.pack(anchor='nw', pady=10)
# 打印选中内容的按钮
Button(root, text='print sel', command=print_sel).pack(anchor='nw')
# 获取索引的按钮
Button(root, text='index', command=print_index).pack(anchor='nw', pady=5)

root.mainloop()