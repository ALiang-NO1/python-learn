from pynput.keyboard import Key, Controller
import time

keyboard = Controller()
# 按下空格和释放空格
# Press and release space
keyboard.press(Key.space)
keyboard.release(Key.space)
# 按下a键和释放a键
# Type a lower case A ;this will work even if no key on the physical keyboard is labelled 'A'
keyboard.press('e')
keyboard.release('e')

with keyboard.pressed(Key.cmd):
    keyboard.press('r')
    keyboard.release('r')

# type 'hello world ' using the shortcut type method
keyboard.type('hello world')