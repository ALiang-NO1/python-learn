from tkinter import *
from tkinter.colorchooser import askcolor

win_width = 900
win_height = 450
class Application(Frame):
    def __init__(self, master=None):
        super().__init__(master)     # super代表父类的定义，而不是父类对象
        self.master = master
        self.x = 0
        self.y = 0
        self.fgcolor = 'red'
        self.lastDraw = 0
        self.startDrawFlag = False
        self.pack()
        self.createWidget()

    def createWidget(self):
        # 创建绘图区
        self.drawpad = Canvas(root, width=win_width, height=win_height, bg='silver'); self.drawpad.pack()
        # 创建按钮                                                   # 打包按钮
        self.btn_bg = Button(root, text="背景", name='bgcolor');    self.btn_bg.pack(side='left', padx='10')
        self.btn_pen = Button(root, text="画笔", name='pen');       self.btn_pen.pack(side='left', padx='10')
        self.btn_rect = Button(root, text="矩形", name='rect');     self.btn_rect.pack(side='left', padx='10')
        self.btn_clear = Button(root, text="清屏", name='clear');   self.btn_clear.pack(side='left', padx='10')
        self.btn_erasor = Button(root, text="橡皮", name='erasor'); self.btn_erasor.pack(side='left', padx='10')
        self.btn_line = Button(root, text="直线", name='line');     self.btn_line.pack(side='left', padx='10')
        self.btn_arrow = Button(root, text="箭头", name='arrow');   self.btn_arrow.pack(side='left', padx='10')
        self.btn_color = Button(root, text="颜色", name='color');   self.btn_color.pack(side='left', padx='10')
        # 绑定事件
        self.btn_bg.bind('<Button-1>', self.eventManager)  # 点击按钮事件：背景色
        self.btn_line.bind('<Button-1>', self.eventManager)  # 点击按钮事件：直线
        self.btn_arrow.bind('<Button-1>', self.eventManager)  # 点击按钮事件：箭头
        self.btn_rect.bind('<Button-1>', self.eventManager)  # 点击按钮事件：矩形
        self.btn_pen.bind('<Button-1>', self.eventManager)  # 点击按钮事件：画笔
        self.btn_erasor.bind('<Button-1>', self.eventManager)  # 点击按钮事件：橡皮
        self.btn_clear.bind('<Button-1>', self.eventManager)  # 点击按钮事件：清屏
        self.btn_color.bind('<Button-1>', self.eventManager)  # 点击按钮事件：换颜色
        self.drawpad.bind('<ButtonRelease-1>', self.stopDraw)   # 鼠标左键释放事件
        # 绑定颜色快捷键
        root.bind('<KeyPress-r>', self.hotkey)
        root.bind('<KeyPress-g>', self.hotkey)
        root.bind('<KeyPress-b>', self.hotkey)
        root.bind('<KeyPress-y>', self.hotkey)

    def eventManager(self, event):
        self.startDrawFlag = True
        name = event.widget.winfo_name()
        print(name)
        if name == 'line':
            self.drawpad.bind('<B1-Motion>', self.myLine)
        elif name == 'arrow':
            self.drawpad.bind('<B1-Motion>', self.myArrow)
        elif name == 'rect':
            self.drawpad.bind('<B1-Motion>', self.myRect)
        elif name == 'pen':
            self.drawpad.bind('<B1-Motion>', self.myPen)
        elif name == 'erasor':
            self.drawpad.bind('<B1-Motion>', self.myErasor)
        elif name == 'clear':
            self.drawpad.delete('all')
        elif name == 'color':
            fg = askcolor(color=self.fgcolor, title="选择画笔颜色")
            self.fgcolor = fg[1]
        elif name == 'bgcolor':
            bg = askcolor(color=self.fgcolor, title="选择背景颜色")
            self.drawpad['bg'] = bg[1]
            print("背景色bg改为：", bg[1])

    def startDraw(self, event):
        self.drawpad.delete(self.lastDraw)
        if self.startDrawFlag:
            self.startDrawFlag = False
            self.x = event.x
            self.y = event.y

    def stopDraw(self, event):
        self.startDrawFlag = True
        self.lastDraw = 0

    def myLine(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)

    def myArrow(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_line(self.x, self.y, event.x, event.y, arrow=LAST, fill=self.fgcolor)

    def myRect(self, event):
        self.startDraw(event)
        self.lastDraw = self.drawpad.create_rectangle(self.x, self.y, event.x, event.y, outline=self.fgcolor)

    def myPen(self, event):
        self.startDraw(event)
        self.drawpad.create_line(self.x, self.y, event.x, event.y, fill=self.fgcolor)
        self.x = event.x
        self.y = event.y

    def myErasor(self, event):
        self.startDraw(event)
        self.drawpad.create_rectangle(event.x-15, event.y-15, event.x+15, event.y+15,
                                      outline=self.drawpad['bg'], fill=self.drawpad['bg'])
        self.x = event.x
        self.y = event.y

    def hotkey(self, event):
        if event.char == 'r':
            self.fgcolor = 'red'
        elif event.char == 'g':
            self.fgcolor = 'green'
        elif event.char == 'b':
            self.fgcolor = 'blue'
        elif event.char == 'y':
            self.fgcolor = 'yellow'

if __name__ == '__main__':
    root = Tk()
    root.title("画图窗口")
    root.geometry('900x500-100+100')
    app = Application(master=root)
    root.mainloop()