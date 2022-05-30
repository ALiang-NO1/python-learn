import wx


class MyFrame1(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(250, 150))
        panel = wx.Panel(self, -1)
        wx.Button(panel, -1, 'Button1', (0, 0))
        wx.Button(panel, -1, 'Button2', (80, 0))
        wx.Button(panel, -1, 'Button3', (160, 0))


class MyFrame2(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, (-1, -1), wx.Size(250, 100))
        panel = wx.Panel(self, -1)
        box = wx.BoxSizer(wx.HORIZONTAL)  # 不带参数表示默认实例化一个水平尺寸器
        box.Add(wx.Button(panel, -1, 'Button1'), 1)
        box.Add(wx.Button(panel, -1, 'Button2'), 1)
        box.Add(wx.Button(panel, -1, 'Button3'), 1)
        panel.SetSizer(box)  # 设置主尺寸器
        self.Center()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyFrame1(None, -1, 'layout')
        frame.Show()
        frame.Center()
        return True


app = MyApp(0)
app.MainLoop()
