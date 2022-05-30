from multiprocessing import Pool
from queue import Queue
import time


def test(p):
    time.sleep(0.5)
    if p == 100:
        return (p,True)
    else:
        return (p,False)


if __name__ == "__main__":
    pool = Pool(processes=10)
    q = Queue()
    for i in range(500):
        # 将子进程对象存入队列中。
        q.put( pool.apply_async(test, args=(i,)) )  # 维持执行的进程总数为10，当一个进程执行完后添加新进程.
        print(i)
    '''
    因为这里使用的为pool.apply_async异步方法，因此子进程执行的过程中，父进程会执行while，获取返回值并校验。
    '''
    print("======", q.qsize())
    while 1:
        a = q.get().get()
        print(a)
        if a[1]:
            pool.terminate()  # 结束进程池中的所有子进程。
            break
    pool.join()