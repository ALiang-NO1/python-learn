import PySimpleGUI as sg

layout = [[sg.Text('Persistent window')],
          [sg.Input(do_not_clear=True, key='_IN_')],
          [sg.Button('Read'), sg.Exit()]]

window = sg.Window('Window that stays open', layout)

while True:
    event, values = window.Read()
    if event is None or event == 'Exit':
        break
    print(event, values)

window.Close()