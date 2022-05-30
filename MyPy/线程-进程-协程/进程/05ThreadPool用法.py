from multiprocessing.pool import ThreadPool
import time

pool = ThreadPool(2)
def task1():
    time.sleep(1)
    print("任务1完成")

def task2(*args, **kwargs):
    time.sleep(1)
    print("任务2完成:", args, kwargs)

pool.apply_async(task1)
pool.apply_async(task2, args=(1, 2), kwds={'a': 1, 'b': 2})
print("任务提交完成")
pool.close()
pool.join()
print("任务完成")