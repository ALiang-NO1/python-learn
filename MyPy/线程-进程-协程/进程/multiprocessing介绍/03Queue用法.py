import os
import multiprocessing
import time

"""
一些进程使用put()在Queue中放入字符串，这个字符串中包含PID和时间。另一些进程从Queue中取出，并打印自己的PID以及get()的字符串。
"""

def in_queue(queue):
    info = str(os.getpid()) + '(put): ' + str(time.time())
    queue.put(info)

def out_queue(queue, lock):
    info = queue.get()
    lock.acquire()
    print(str(os.getpid()) + ' get: ' + info)
    lock.release()

record1 = []  # 存放输入的进程
record2 = []  # 存放输出的进程
lock = multiprocessing.Lock()
queue = multiprocessing.Queue(3)

if __name__ == '__main__':
    for i in range(3):
        process = multiprocessing.Process(target=in_queue, args=(queue,))
        process.start()
        record1.append(process)

    for i in range(3):
        process = multiprocessing.Process(target=out_queue, args=(queue, lock))
        process.start()
        record2.append(process)

    for p in record1:
        p.join()

    queue.close()  # 没有其他对象进入，关闭队列

    for p in record2:
        p.join()