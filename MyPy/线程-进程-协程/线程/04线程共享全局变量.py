from threading import Thread, Lock

"""锁的优缺点
1、确保了某段关键代码只能由一个线程从头到尾完整地执行
2、阻止了多线程并发执行，包含锁的某段代码实际上只能以单线程模式执行，效率就大大地下降了。
3、由于可以存在多个锁，不同的线程持有不同的锁，并试图获取对方持有的锁时，可能会造成死锁，导致多个线程全部挂起，既不能执行，也无法结束，只能靠操作系统强制终止。
"""

num = 0
lock = Lock()

def test(n):
    global num
    num += n
    num -= n

def run(n):
    for i in range(100000):
        # lock.acquire()
        test(n)
        # lock.release()

if __name__ == '__main__':
    # 两个线程同时一存一取，就可能导致余额不对
    t1 = Thread(target=run, args=(3,))
    t2 = Thread(target=run, args=(8,))
    t1.start()
    t2.start()
    t1.join()
    t2.join()
print(num)