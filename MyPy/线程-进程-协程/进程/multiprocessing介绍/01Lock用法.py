import os
import threading
import multiprocessing

print('————Main pid: %s' % os.getpid())

def worker(type, lock):  # （类型，锁）
    lock.acquire()
    print(type, os.getpid())
    lock.release()

# multi-thread
t_record = []
t_lock = threading.Lock()

# multi-process
p_record = []
p_lock = multiprocessing.Lock()

if __name__ == '__main__':
    for i in range(5):
        thread = threading.Thread(target=worker, args=('thread', t_lock))
        thread.start()
        t_record.append(thread)
    
    for thread in t_record:
        thread.join()
        
    for i in range(5):
        process = multiprocessing.Process(target=worker, args=('process', p_lock))
        process.start()
        p_record.append(process)

    for process in p_record:
        process.join()