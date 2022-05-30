from multiprocessing import Process

number = 0
def change():   # 为拟创建的子进程1提供方法
    print('子进程1开始运行...')
    global number
    for i in range(5000):
        number += 1
    print('把number加5000次一等于:%d' % number)
    print('子进程1结束')

def changes():  # 为拟创建的子进程2提供方法
    print('子进程2开始运行...')
    global number
    for i in range(10000):
        number += 1
    print('把number加10000次一等于:%d' % number)
    print('子进程2结束')

if __name__ == '__main__':
    process_one = Process(target=change)
    process_one.start()     # 启动进程
    process_one.join()  # 等待进程执行结束
    process_two = Process(target=changes)
    process_two.start()     # 启动进程
    process_two.join()      # 等待进程执行结束
    print('number最后为:%d' % number)