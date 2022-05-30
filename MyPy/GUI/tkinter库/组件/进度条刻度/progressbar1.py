"""测试进度条属性"""
from tkinter.ttk import Progressbar
import tkinter

def run():
    pb2.start()

def update():
    global bytes
    if bytes <= max_bytes:
        pb1['value'] = bytes
        bytes += 50
        pb1.after(500, update)
        # root.update()  重绘窗口

def stop():
    value = pb2['value']
    pb2.stop()
    pb2['value']= value

root = tkinter.Tk()
root.title('进度条测试')
root.geometry('240x200-100+100')

# 规定的进度条
pb1 = Progressbar(root, length=200, mode='indeterminate', orient='horizontal')
pb1.pack(anchor='w', padx=5, pady=5)
# 进度值最大值
pb1['maximum'] = 1000
# 进度值初始值
pb1['value'] = 100
bytes = pb1['value']
max_bytes = 1000
# 开始按钮
btn_run = tkinter.Button(root, text='Run', width=6, command=update)
btn_run.pack(padx=5, pady=5, anchor='nw')

# 横排 长度200 来回滚动的
pb2 = Progressbar(root, mode='determinate', orient=tkinter.HORIZONTAL)
pb2.pack(padx=5, side='left')
# 开始按钮
btn_run = tkinter.Button(root, text='Run', width=6, command=run)
btn_run.pack(padx=5, pady=5, side='left')
# 终止按钮
btn_stop = tkinter.Button(root, text='Stop', width=6, command=stop)
btn_stop.pack(pady=5, side='left')

root.mainloop()