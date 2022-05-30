import wx

app = wx.App()
frame = wx.Frame(None, title='GUI Test Editer', pos=(800, 200), size=(500, 400))

def openfile(event):
    path = path_text.GetValue()
    with open(path, 'r', encoding='utf-8') as f:
        content_text.SetValue(f.read())

path_text = wx.TextCtrl(frame, pos=(5, 5))
open_button = wx.Button(frame, label='打开', pos=(370, 5), size=(50, 24))
open_button.Bind(wx.EVT_BUTTON, openfile)
save_button = wx.Button(frame, label='保存', pos=(370, 5), size=(50, 24))
content_text = wx.TextCtrl(frame, pos=(5, 39), size=(475, 300), style=wx.TE_MULTILINE)
# wx.TE_MULTILINE可以实现以滚动条方式多行显示文本,若不加此功能文本文档显示为一行

frame.Show()
app.MainLoop()