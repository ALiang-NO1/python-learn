import PySimpleGUI as sg

layout = [[sg.Text('My one-shot window.')],
          [sg.InputText()],  # 类似于 python 内置函数 input
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Window Title', layout)

event, values = window.Read()
window.Close()  # 切记

text_input = values[0]  # 输入框文本
print(event, text_input)
