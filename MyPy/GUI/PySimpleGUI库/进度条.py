import PySimpleGUI as sg
import time

my_list = [1, 2, 3, 4, 5, 6, 7, 8]
# for i, item in enumerate(my_list):
#     # title, current_value, max_value, key='OK for 1 meter', *args, orientation='v', bar_color=(None, None),
#     # button_color=None, size=DEFAULT_PROGRESS_BAR_SIZE, border_width=None, grab_anywhere=False, no_titlebar=False
#     sg.one_line_progress_meter('This is my progress meter! ', i+1, len(my_list))
#     time.sleep(1)

progressbar = [[sg.ProgressBar(len(my_list), orientation='h', size=(51, 10), key='progressbar')]]
output_win = [[sg.Output(size=(78, 20))]]
layout = [
        [sg.Frame('Progress', layout=progressbar)],
        [sg.Frame('Output', layout=output_win)],
        [sg.Submit('Start'), sg.Cancel()]]
window = sg.Window('Custom Progress Meter', layout)
progress_bar = window[progressbar]
while True:
    event, values = window.read(timeout=10)
    if event == 'Cancel' or event is None:
        break
    elif event == 'Start':
        for i, item in enumerate(my_list):
            print(item)
            time.sleep(1)
            progress_bar.UpdateBar(i + 1)
window.close()
