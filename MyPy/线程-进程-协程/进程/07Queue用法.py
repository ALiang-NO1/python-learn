from multiprocessing import Process, Queue
import time
import datetime

# 往停车场中停入车辆
def park(x):  # x: 队列
    if not x.full():
        for i in range(5):
            car = '车辆' + str(i)
            x.put(car)      # 把五辆车放入pool
            print('停入：%s 时间:%s' % (car, datetime.datetime.now()))
# 开走车辆
def drive(x):  # x: 队列
    time.sleep(2)   # 休眠2s
    while not x.empty():
        print('开走：%s 时间:%s' % (x.get(True, 3), datetime.datetime.now()))

if __name__ == '__main__':
    x = Queue()     # 创建一个队列
    p = Process(target=park, args=(x,))      # 创建一个进程，并放入队列中
    d = Process(target=drive, args=(x,))     # 创建一个进程，并放入队列中
    p.start()    # 启动
    d.start()    # 启动
    # p.join()
    # d.join()