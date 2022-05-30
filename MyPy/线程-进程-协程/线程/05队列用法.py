"""多个线程之间的数据是共享的，多个线程进行数据交换的时候，不能够保证数据的安全性和一致性，所以当多个线程需要进行数据交换的时候，队列就出现了。
队列可以完美解决线程间的数据交换，保证线程间数据的安全性和一致性(简单的来说就是多线程需要加锁，很可能会造成死锁，而queue自带锁"""

import time
import queue
from queue import Queue
from threading import Thread
from random import randint

# my_queue = Queue(3)   # 3个队列
# def f1(my_queus):
#     for i in range(3):
#         num = randint(0, 10)
#         print("输入数字：", num)
#         my_queue.put(num)
#
# def f2(my_queus):
#     for i in range(3):
#         time.sleep(1)
#         num = my_queue.get()
#         print("获取数字：", num)
#
# t1 = Thread(target=f1, args=(my_queue,))
# t2 = Thread(target=f2, args=(my_queue,))
# t1.start()
# t2.start()
# t1.join()
# t2.join()

print("----------先进先出------------")
# 实例化一个队列，可以在指定队列大小
q = Queue(5)  # 指定一个长度为5的队列, 若maxsize<=0则不限制队列大小
for date in range(5):
    # 入队一个数据data
    q.put(date)
    if q.full():  # 判断队列是否为空，是否满
        print('队列满')

while not q.empty():
    # 出队并赋值给item
    item = q.get()
    print("获取数据：", item)
print(q.empty())

print("----------后进先出------------")
q = queue.LifoQueue()  # 创建 LifoQueue 队列
for i in range(3):
    q.put(i)  # 在队列中依次插入0、1、2元素
for i in range(3):
    print("输出数据：", q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为2、1、0

print("----------排序输出------------")
q = queue.PriorityQueue()  # 创建 PriorityQueue 队列
data1 = (1, 'python')
data2 = (3, '-')
data3 = (2, '100')
datas = (data2, data3, data1)
for data in datas:
    q.put(data)  # 在队列中依次插入元素 data2、data3、data1
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为 data1、data2、data3

print("----------简单队列------------")
q = queue.SimpleQueue()  # 创建 SimpleQueue 队列
for i in range(3):
    q.put(i)  # 在队列中依次插入0、1、2元素
for i in range(3):
    print(q.get())  # 依次从队列中取出插入的元素，数据元素输出顺序为0、1、2

print("----------Empty异常------------")
try:
    q = queue.Queue(3)  # 设置队列上限为3
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-')  # 在队列中插入字符串 '-'
    q.put('100')  # 在队列中插入字符串 '100'
    for i in range(4):  # 从队列中取数据，取出次数为4次，引发 queue.Empty 异常
        print(q.get(block=False))
except queue.Empty as e:
    print('wrong:', e)

print("----------Full异常------------")
try:
    q = queue.Queue(3)  # 设置队列上限为3
    q.put('python')  # 在队列中插入字符串 'python'
    q.put('-')  # 在队列中插入字符串 '-'
    q.put('100')  # 在队列中插入字符串 '100'
    q.put('stay hungry, stay foolish', block=False)  # 队列已满，继续往队列中放入数据，引发 queue.Full 异常
except queue.Full:
    print('queue.Full')
