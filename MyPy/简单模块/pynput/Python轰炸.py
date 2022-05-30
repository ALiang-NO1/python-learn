import time
from pynput.keyboard import Controller as ctrl
from pynput.mouse import Button, Controller

def keyboard_input(string):
    """
    :param string: 你想要发送的信息
    :return: None
    """
    keyboard = ctrl()  # 开始控制键盘
    keyboard.type(string)  # 键盘输入string


def mouse_click():  # 点击发送消息
    mouse = Controller()  # 开始控制鼠标
    mouse.press(Button.left)  # 按住鼠标左键
    mouse.release(Button.left)  # 放开鼠标左键


def main(number, string):  # 参数分别表示你要发多少条信息和发送的内容
    time.sleep(5)  # 此时暂停5s，方便你打开聊天窗，并把鼠标停放在发送按钮上
    for i in range(number):  # 用循环来控制你发送多少条消息
        keyboard_input(string + str(i))
        mouse_click()
        time.sleep(0.2)


if __name__ == '__main__':
    main(500, "这里输入轰炸语句")
