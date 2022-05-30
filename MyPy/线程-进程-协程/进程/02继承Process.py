import multiprocessing
import time
import datetime
import os

class MyProcess(multiprocessing.Process):
    def __init__(self, name=None):     # 使用父类中的初始化方法
        multiprocessing.Process.__init__(self)    # 接受参数
        if name:    # 判断传递的参数是否存在
            self.name = name

    def run(self):
        print('子进程开始的时间为：', datetime.datetime.now())
        print('子进程 %s 正在执行...' % os.getpid())
        time.sleep(5)
        print('子进程执行完毕的结束时间为：', datetime.datetime.now())

if __name__ == '__main__':
    print('父进程PID为：', os.getpid())
    print('父进程开始执行的时间为:', datetime.datetime.now())
    process_one = MyProcess()
    process_one.start()    # 启动进程
    process_one.join()  # 等待进程执行结束
    print('父进程结束执行的时间为:', datetime.datetime.now())