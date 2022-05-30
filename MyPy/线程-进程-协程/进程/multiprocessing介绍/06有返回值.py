from multiprocessing import Pool
import time

def func(msg):
    print('msg: %s' % msg)
    time.sleep(1)
    print('func() ends.')
    return msg

p = Pool(processes=3)

result = []
for i in range(1, 3):
    msg = 'The i-value is %d' % i
    res = p.apply_async(func, (msg,))
    result.append(res)

print('pool starts...')
p.close()
p.join()
for res in result:
    # res.get()方法是堵塞的。只有子进程执行完毕并返回数据时 res.get()方法才会执行，否则主进程堵塞，并等待
    print('sub_process returns: %s' % res.get())
print('sub_process ends.')