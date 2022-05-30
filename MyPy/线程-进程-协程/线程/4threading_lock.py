import time
import threading
from threading import Semaphore
import random

writerminute = Semaphore(1)  # 添加计数器
readerminute = Semaphore(1)  # 添加计数器
readercount = 0
sleept = 1

def reader(i):
    """我们先对读者函数进行理解——首先当第一个线程开始的时候，读者开始阅读，进入一个函数判断，如果当前没有读者在读，首先把写者计数器给锁定，然后
     进入阅读；读完之后判断是否还有读者在读，如果没有人在读，就解开锁定。然后是写者函数——最后在主程序中，我们通过随机数产生八个数字，把1看成读者，
     0看成写者，第一个进入队列的首先进行操作，后续的全部排队，如果第一个是写者，那么后面的所有人都不能进行操作，只有等待；如果第一个是读者，
     那么后面的人先进行等待，然后是读者优先进行阅读。"""
    print('读者' + str(i) + ' 等待阅读\n', end='')
    readerminute.acquire()  # 计数器+1
    global readercount
    if readercount == 0:
        writerminute.acquire()  # 计数器+1
    readercount += 1  # 阅读人数+1
    readerminute.release()  # 计数器-1
    print('读者' + str(i) + ' 正在阅读\n', end='')
    time.sleep(sleept)
    print('读者' + str(i) + ' 结束阅读\n', end='')
    readerminute.acquire()
    readercount -= 1  # 读完-1
    if readercount == 0:
        writerminute.release()
    readerminute.release()

def writer(i):
    print('写者' + str(i) + ' 等待去写\n', end='')
    writerminute.acquire()  # +1
    print('写者' + str(i) + ' 正在写\n', end='')
    time.sleep(sleept)  # 读
    print('写者' + str(i) + ' 完成写作\n', end='')
    writerminute.release()  # 结束-1

if __name__ == '__main__':
    list = []
    for i in range(8):
        list.append(random.randint(0, 1))
    print(list)
    # 创建了一个人数者为8的列表，1为读者，0为写。
    # 首位优先进行阅读或写作，后续等待。
    rindex = 1
    windex = 1
    for i in list:
        if i == 0:
            t = threading.Thread(target=reader, args=(rindex,))
            rindex += 1
            t.start()
        else:
            t = threading.Thread(target=writer, args=(windex,))
            windex += 1
            t.start()