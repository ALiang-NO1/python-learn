import time
from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()
lock3 = Lock()
lock2.acquire()
lock3.acquire()
class Task1(Thread):
    def run(self):
        while True:
            print('lock1：%s' % lock1)
            if lock1.acquire():
                print('task1')
                time.sleep(1)
                lock2.release()
class Task2(Thread):
    def run(self):
        while True:
            print('lock2：%s' % lock2)
            if lock2.acquire():
                print('task2')
                time.sleep(1)
                lock3.release()
class Task3(Thread):
    def run(self):
        while True:
            print('lock3：%s' % lock3)
            if lock3.acquire():
                print('task3')
                time.sleep(1)
                lock1.release()
if __name__ == '__main__':
    t1 = Task1()
    t2 = Task2()
    t3 = Task3()
    t1.start()
    t2.start()
    t3.start()