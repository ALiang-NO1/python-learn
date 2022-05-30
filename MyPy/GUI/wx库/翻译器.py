import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "翻译器", size=(600, 200))
        panel = wx.Panel(self)# 创建一个画布，然后创建功能区并放到画布上
        # 创建一个标题, 放在panel中
        self.title = wx.StaticText(panel, label='简单翻译器')
        # 创建一个静态文本，放在panel中
        self.translate = wx.StaticText(panel, label='翻译内容:')
        # 创建一个输入文本框，放在panel中
        self.tran_slate = wx.TextCtrl(panel, style=wx.TE_LEFT)
        # 创建一个翻译按钮，放在panel中
        self.button_ts = wx.Button(panel, label='翻译')
        # 创建一个关闭按钮，放在panel中
        self.button_shutdown = wx.Button(panel, label='关闭')
        container_one = wx.BoxSizer(wx.HORIZONTAL)
        # 把静态文本和输入文本框放在这个BoxSizer当中
        container_one.Add(self.translate, proportion=0, flag=wx.ALL, border=7)
        container_one.Add(self.tran_slate, proportion=1, flag=wx.ALL, border=7)
        # 再创建一个水平排布的BoxSizer
        container_two = wx.BoxSizer(wx.HORIZONTAL)
        # 把两个按钮放到这个BoxSizer中
        container_two.Add(self.button_ts, proportion=0, flag=wx.ALIGN_CENTER, border=4)
        container_two.Add(self.button_shutdown, proportion=0, flag=wx.ALIGN_CENTER, border=4)
        # 创建一个竖直排布的BoxSizer
        sizers = wx.BoxSizer(wx.VERTICAL)
        # 把上面的内容都放到这个BoxSizer当中即可
        sizers.Add(self.title, proportion=0, flag=wx.BOTTOM|wx.TOP|wx.ALIGN_CENTER, border=10)
        sizers.Add(container_one, proportion=0, flag =wx.EXPAND|wx.LEFT|wx.RIGHT, border=40)
        sizers.Add(container_two, proportion=0, flag=wx.ALIGN_CENTER|wx.TOP, border=10)
        panel.SetSizer(sizers)
if __name__ == "__main__":
    app = wx.App()
    frame = MyFrame()
    frame.Show()
    app.MainLoop()