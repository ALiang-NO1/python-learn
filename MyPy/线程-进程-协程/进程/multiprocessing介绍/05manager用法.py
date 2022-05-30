# Manager是通过共享进程的方式共享数据。
from multiprocessing import Process, Manager

def func(shareList, shareValue, shareDict, lock):
    with lock:
        shareValue.value += 1
        shareDict[1] = '1'
        shareDict[2] = '2'
        for i in range(len(shareList)):
            shareList[i] += 1

if __name__ == '__main__':
    manager = Manager()
    list1 = manager.list([x for x in range(1, 6)])
    dict1 = manager.dict()
    array1 = manager.Array('i', range(10))
    value1 = manager.Value('i', 1)
    lock = manager.Lock()
    proc = [Process(target=func, args=(list1, value1, dict1, lock)) for i in range(20)]
    for p in proc:
        p.start()
    for p in proc:
        p.join()
    print(list1)
    print(dict1)
    print(array1)
    print(value1)