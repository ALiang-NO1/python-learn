from multiprocessing.dummy import Pool
import time

sum = 0
def calc_power2(num):
    global sum
    sum += num
    time.sleep(1)

start = time.time()
pool = Pool(10)
origin_nums = [x for x in range(25)]
print(origin_nums)
pool.map(calc_power2, origin_nums)
lag = time.time() - start
print('time:', lag)
print('sum:', sum)