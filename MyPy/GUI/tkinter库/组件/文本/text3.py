"""测试文本框（用了滚动文本框）的复制、粘贴、剪切、查找 及 文件打开、保存功能"""
from tkinter import Tk, Text, Menu, Entry, Button, SEL_FIRST, SEL_LAST, TclError
from tkinter.filedialog import askopenfile, asksaveasfile
from tkinter.scrolledtext import ScrolledText
from PIL import Image, ImageTk

root = Tk()
root.title('文本框测试')
root.geometry('400x220-100+100')
root.rowconfigure(1, weight=1)
root.columnconfigure(0, weight=1)

def paste():
    text.event_generate('<<Paste>>')
    # try:
    #     copied_text = text.selection_get(selection='CLIPBOARD')
    #     text.insert('insert', copied_text)
    # except TclError:
    #     print('剪切板没有数据！')

def copy():
    text.event_generate('<<Copy>>')
    # try:
    #     text.clipboard_clear()
    #     copied_text = text.get(SEL_FIRST, SEL_LAST)
    #     text.clipboard_append(copied_text)
    # except TclError:
    #     print('没有选取！')

def cut():
    text.event_generate('<<Cut>>')
    # copy()
    # text.delete(SEL_FIRST, SEL_LAST)

def show_menu(event):
    menu.post(event.x_root, event.y_root)

def undo():
    try:
        text.edit_undo()
    except:
        print('先前没有动作！')

def redo():
    try:
        text.edit_redo()
    except:
        print('先前没有动作！')

def search():
    text.tag_remove('found', '1.0', 'end')
    start = '1.0'
    key = entry.get()
    if len(key.strip()) == 0:
        return
    while True:
        pos = text.search(key, start, 'end')
        if pos == '':
            break
        text.tag_add('found', pos, '%s+%dc' % (pos, len(key)))
        start = '%s+%dc' % (pos, len(key))
        print(start)

def newFile():
    text.delete('1.0', 'end')
    root.title('untitled')

def openFile():
    filename = askopenfile().name
    if filename == '':
        return
    with open(filename, 'r', encoding='utf8') as f:
        content = f.read()
    text.delete('1.0', 'end')
    text.insert('end', content)
    root.title(filename)

def saveFile():
    asksaveasfile(title='保存文件', initialdir='E:\\', initialfile='untitled', filetype=[("untitled", ".txt")])
    # content = text.get('1.0', 'end')
    # filename = 'untitled.txt'
    # with open(filename, 'w', encoding='utf8') as f:
    #     f.write(content)
    #     root.title(filename)

# 搜索框
entry = Entry(root)
entry.grid(row=0, column=0, padx=5, pady=3, sticky='w')
# 开始查找按钮
Button(root, text='查找', command=search, height=1).grid(row=0, column=1, pady=3, sticky='nw')  # 如何调整与搜索栏的间隔？？
# 功能菜单
menu = Menu(root, tearoff=False)
file_menu = Menu(menu, tearoff=False)
file_menu.add_command(label='New File', command=newFile)
file_menu.add_command(label='Open File', command=openFile)
file_menu.add_command(label='Save File', command=saveFile)
menu.add_cascade(label='File', menu=file_menu)
menu.add_command(label='Cut', command=cut)
menu.add_command(label='Copy', command=copy)
menu.add_command(label='Paste', command=paste)
menu.add_command(label='Undo', command=undo)
menu.add_command(label='Redo', command=redo)
root['menu'] = menu
root.bind('<Button-3>', show_menu)

text = ScrolledText(root, undo=True, insertbackground='brown', selectbackground='skyblue', selectforeground='red')
text.grid(row=1, column=0, columnspan=2, padx=5, sticky='nw')  # 放置文本框，如何用grid使其可以随缩放改变大小？？
text.insert('end', 'Test test!\n')
text.insert('end', '有志者，事竟成！————一位著名的诗人***!\n')
# 添加查找标签
text.tag_config('found', background='yellow')
# 插入图片
img = Image.open(r'..\pic.gif')
tk_img = ImageTk.PhotoImage(img)
text.image_create('end', image=tk_img)
# print(text.image_names())  # 列出所有图片名（元组）

root.mainloop()