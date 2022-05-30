import sys
import PySimpleGUI as sg

if len(sys.argv) == 1:
    event, (fname,) = sg.Window('My Script').Layout([[sg.Text('Document to open')],
         [sg.In(), sg.FileBrowse()], [sg.CloseButton('Open'), sg.CloseButton('Cancel')]]).Read()
else:
    fname = sys.argv[1]
if not fname:
    sg.Popup("Cancel", "No filename supplied")
    raise SystemExit("Cancelling: no filename supplied")
print(event, fname)

"""
layout = [[sg.Text('Enter 2 files to comare')],
          [sg.Text('File 1', size=(8, 1)), sg.InputText(), sg.FileBrowse()],
          [sg.Text('File 2', size=(8, 1)), sg.InputText(), sg.FileBrowse()],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('File Compare', layout)

event, values = window.Read()
window.Close()
print(event, values)
"""