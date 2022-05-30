import threading
import time

class MyThread(threading.Thread):
    def __init__(self, name=None):
        super().__init__(name=name)

    def run(self):
        running = True
        while running:
            print('线程开始工作')
            time.sleep(2)
            print('工作完毕')
            s = input('是否停止执行，确认停止请输入q:')
            if s == 'q':
                running = False

if __name__ == '__main__':
    thread = MyThread()
    thread.start()