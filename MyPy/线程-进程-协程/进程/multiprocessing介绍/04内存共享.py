"""测试资源是否在两个进程之间共享"""
import multiprocessing as mp

def func(a, arr):
    a.value = 3.14
    for i in range(len(arr)):
        arr[i] = 0
    a.value = 0

if __name__ == '__main__':
    num = mp.Value('d', 1.0)  # 双精度数(d), 并初始化为1.0
    arr = mp.Array('i', range(10))  # 类似于C中的数组，有固定的类型(i, 也就是整数)
    p = mp.Process(target=func, args=(num, arr))
    p.start()
    p.join()
    print(num.value)
    print(arr[:])