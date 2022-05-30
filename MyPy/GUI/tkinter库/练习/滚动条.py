from tkinter import *

# 创建窗口
review = Tk()
# 标题
review.title("滚动条设计")
# 窗口基于屏幕的坐标 +x轴+y轴
review.geometry("-100+100")
# 创建lab标签
labelx = Label(review, text="文本框实现", font=("王羲之书法字体", 20))
# 显示lab标签 网格布局 sticky=W #左对齐 E为右对齐 默认为中间对齐
labelx.grid(row=0, column=0)

# ----------------------------------------------------------------------------

# 创建一个纵向滚动的滚动条,打包到窗口右侧，铺满Y方向
scrollbar = Scrollbar(review, orient=VERTICAL, bg="red")  # orient默认为纵向
scrollbar.grid(column=1)

# 打包一个文本域到窗口，y方向滚动文本的监听丢给滚动条的set函数（文本域主动关联滚动条）
# 高度和宽度确定的是字符个数（win)
text = Text(review, width=50, height=10, yscrollcommand=scrollbar.set)
text.grid(row=1, column=0)

# 拉动滚动条时，改变文本域在y方向上的视图（滚动条主动关联文本域）
scrollbar.config(command=text.yview)

# -------------------------------------------------------------------------

# 消息循环 显示窗口
review.mainloop()
