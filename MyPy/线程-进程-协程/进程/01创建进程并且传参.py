from multiprocessing import Process

def run_test(name, **kwargs):
    print("子进程正在运行,name的值：%s" % name)
    print("字典kwargs:", kwargs)

if __name__ == '__main__':
    print("主程序正在运行————")
    p = Process(target=run_test, args=('test',), kwargs={'key': 12})
    p.start()