import wx


class MyToolBar(wx.Frame):
    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, ID, title, wx.DefaultPosition, wx.Size(350, 250))
        vbox = wx.BoxSizer(wx.VERTICAL)  # wx.VERTICAL参数表示实例化一个垂直尺寸器
        toolbar = wx.ToolBar(self, -1, style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        toolbar.AddTool(1, wx.Image('v.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'New', '')
        toolbar.AddTool(2, wx.Image('v.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Open', '')
        toolbar.AddTool(3, wx.Image('v.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Save', '')
        toolbar.AddSeparator()
        toolbar.AddTool(4, wx.Image('v.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap(), 'Exit', '')
        toolbar.Realize()

        vbox.Add(toolbar, 0, border=5)
        self.SetSizer(vbox)
        self.statusBar = self.CreateStatusBar()

        self.Center()

        wx.EVT_TOOL(self, 1, self.new)
        wx.EVT_TOOL(self, 2, self.open)
        wx.EVT_TOOL(self, 3, self.save)
        wx.EVT_TOOL(self, 4, self.exit)

    def new(self, event):
        self.statusBar.SetStatusText('New Command')

    def open(self, event):
        self.statusBar.SetStatusText('Open Command')

    def save(self, event):
        self.statusBar.SetStatusText('Save Command')

    def exit(self, event):
        self.Close()


class MyApp(wx.App):
    def OnInit(self):
        frame = MyToolBar(None, -1, 'toolbar')
        frame.Show()
        return True


app = MyApp()
app.MainLoop()
