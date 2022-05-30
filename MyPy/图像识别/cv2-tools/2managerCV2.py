from cv2_tools.Management import ManagerCV2
import cv2

managerCV2 = ManagerCV2(cv2.VideoCapture(0), is_stream=True, key_stroke=27, wait_key=1, fps_limit=60)
last_keystroke = 27     # esc=27
for frame in managerCV2:
    if last_keystroke != -1:
        print(last_keystroke)
        cv2.imshow('Easy button checker', frame)
        last_keystroke = input()
cv2.destroyAllWindows()