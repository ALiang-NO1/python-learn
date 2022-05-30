from tkinter import Tk, Scale, Label, HORIZONTAL, VERTICAL

root = Tk()
root.geometry('300x300-100+100')

# 获取值的滑块
def test(value):
    print("滑块的值：", value)
    font = ("方正舒体", value)
    logo.config(font=font)

# command=test 中，事件自动传入滑块值作为参数
sc = Scale(root, to=50, length=200, tickinterval=5, orient='horizontal', takefocus=1, command=test)
sc.pack(pady=2)
sc.set(17)
logo = Label(root, text="百战程序员", font="方正舒体", width=10, height=1, bg='black', fg='white')
logo.pack()

# 有颜色，无标题滑块
def print_selection(v):
    label.config(text='you have selected ' + v)

label = Label(root, bg='yellow', width=20, text='empty')
label.pack(pady=2)
Scale(root, label='try me', from_=5, to=11, orient=HORIZONTAL, troughcolor='pink',
      length=200, showvalue=0, tickinterval=3, resolution=0.01, command=print_selection).pack()

# 调色滑块
def update_bg():
    red = rSlider.get()
    green = gSlider.get()
    blue = bSlider.get()
    # print('R=%d, G=%d, B=%d' % (red, green, blue))
    color = '#%02x%02x%02x' % (red, green, blue)
    # print(color)
    root.config(bg=color)
    color_label.config(text=color)

rSlider = Scale(root, from_=0, to=255, command=update_bg, orient=VERTICAL, width=10, troughcolor='red')
gSlider = Scale(root, from_=0, to=255, command=update_bg, orient=VERTICAL, width=10, troughcolor='green')
bSlider = Scale(root, from_=0, to=255, command=update_bg, orient=VERTICAL, width=10, troughcolor='blue')
gSlider.set(125)
rSlider.pack(padx=2, pady=2, side='left', anchor='n')
gSlider.pack(padx=2, pady=2, side='left', anchor='n')
bSlider.pack(padx=2, pady=2, side='left', anchor='n')
color_label = Label(root, text='', width=10, height=3, bg='gold', font='黑体 18')
color_label.pack(side='left')

root.mainloop()