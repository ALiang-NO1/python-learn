import wx

app = wx.App()
frame = wx.Frame(None, -1, '')

frame.SetTitle('simple.py')  # 置窗口标题。只可用于框架和对话框
frame.SetPosition(wx.Point(0, 0))  # 设置窗口出现的位置。
frame.SetSize(wx.Size(300, 250))  # 设置窗口的尺寸。
frame.SetToolTip(wx.ToolTip('This is a frame'))  # 为窗口添加提示。
frame.SetCursor(wx.Cursor(wx.CURSOR_MAGNIFIER))  # 设置窗口的鼠标指针样式。
frame.Show()  # 显示或隐藏窗口。其中的参数可以为 True 或False
app.MainLoop()
