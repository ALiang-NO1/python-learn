import time
from concurrent.futures.thread import ThreadPoolExecutor

def func(value):
    time.sleep(1)
    print(value)

pool = ThreadPoolExecutor(max_workers=5)
for i in range(3):
    fut = pool.submit(func, str(i+1)+".Hello")
