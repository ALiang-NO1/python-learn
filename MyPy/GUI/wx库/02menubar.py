import wx

app = wx.App()
frame = wx.Frame(None, -1, 'IconTest', wx.DefaultPosition, wx.Size(350, 300))
frame.SetIcon(wx.Icon('icon.bmp', wx.BITMAP_TYPE_ICO))
frame.Center()

menubar = wx.MenuBar()  # 创建菜单栏
file = wx.Menu()  # 创建菜单
edit = wx.Menu()
help = wx.Menu()
file.Append(101, '&Open', '&Open a new document')  # 添加菜单项
file.Append(102, '&save', 'save a new document')
file.AppendSeparator()  # 添加分割线
menubar.Append(file, '&File')
menubar.Append(edit, '&Edit')
menubar.Append(help, '&Help')
frame.SetMenuBar(menubar)

frame.Show()
app.MainLoop()
