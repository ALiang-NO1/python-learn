from tkinter import Tk, Label, Listbox, StringVar, Button

window = Tk()
window.title("GUI程序测试")
window.geometry('300x300-100+100')

def print_selection():  # 在标签中显示选择的内容
    slt = lb.curselection()
    if slt:
        print('选择的：', slt)
        print('是否包含第四个：', lb.select_includes(3))  # 是否显示第四个元素
        value = ''
        for s in slt:
            value += str(lb.get(s)) + '、'  # get 里面是索引！获取的内容可以是整数
        var1.set(value)

def print_sel(event):
    obj = event.widget
    indexs = obj.curselection()
    sel = ''
    for index in indexs:
        sel += str(obj.get(index)) + '  '
    label['text'] = '选择的项\n' + sel

# 显示选择项的标签
label = Label(window, bg='beige', fg='red', width=20, relief='ridge')
label.pack()

var2 = StringVar()
var2.set((11, 22, 33, 44))  # 将设置为列表盒子的内容
lb = Listbox(window, listvariable=var2, selectmode='multiple')
list_items = [1, 2, 3, 4]
for item in list_items:
    lb.insert('end', item)
lb.insert(0, 'first')  # 第一行插入 first
lb.insert(2, 'second')  # 第三行插入 second
lb.delete(2)  # 删除第三个
lb.select_set(0)  # 设置选中第一个
lb.pack(pady=4)
lb.bind('<<ListboxSelect>>', print_sel)  # 绑定事件

var1 = StringVar()
Label(window, bg='yellow', textvariable=var1, width=20).pack(pady=4)

b1 = Button(window, text='print selection', width=15, height=2, command=print_selection)
b1.pack()

window.mainloop()