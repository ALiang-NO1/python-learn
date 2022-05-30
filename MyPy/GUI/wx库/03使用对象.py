import wx

class MyMenu(wx.Frame):
    def quit(self, event):
        self.Close()

    def __init__(self, parent, ID, title):
        wx.Frame.__init__(self, parent, -1, title, wx.DefaultPosition, wx.Size(400, 200))
        menubar = wx.MenuBar()
        file = wx.Menu()  # 创建菜单
        edit = wx.Menu()
        help = wx.Menu()
        file.Append(101, '&Open', '&Open a new document')  # 添加菜单项
        file.Append(102, '&save', 'save a new document')
        menubar.Append(file, '&File')
        menubar.Append(edit, '&Edit')
        menubar.Append(help, '&Help')
        self.SetMenuBar(menubar)
        self.Center()   # 将窗口放在屏幕中央

        wx.EVT_MENU(self, 105, self.quit)

        # edit.Append(201, 'check item', wx.ITEM_CHECK)
        quit = wx.MenuItem(file, 105, '&Quit\tCtr+Q', 'Quit the application')
        quit.SetBitmap(wx.Image('v.png', wx.BITMAP_TYPE_PNG).ConvertToBitmap())
        edit.Append(quit)

        submenu = wx.Menu()
        submenu.Append(301, 'radio item1', kind=wx.ITEM_RADIO)
        submenu.Append(302, 'radio item2', kind=wx.ITEM_RADIO)
        submenu.Append(303, 'radio item3', kind=wx.ITEM_RADIO)
        edit.Append(203, 'submenu', submenu)

class MyApp(wx.App):
    def OnInit(self):
        frame = MyMenu(None, -1, 'menubarTest')
        frame.Show(True)
        return True
app = MyApp(0)
app.MainLoop()