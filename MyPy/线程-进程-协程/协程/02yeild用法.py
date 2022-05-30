# def gen():
#     n = 0
#     while True:
#         yield n
#         n += 1
#         print('n加了1，n的值为：', n)
# g = gen()
# print('gen():', g)
# for i in range(3):
#     print('next:', next(g))

from time import sleep
print("----------委派生成器-------")
# 子生成器
def average_gen():
    count = 0
    total = 0
    average = 0
    while True:
        print('start...')
        sleep(2)
        new_num = yield average
        count += 1
        total += new_num
        average = total/count
        print('end!')

# 委托生成器
def proxy_gen():
    while True:
        yield from average_gen()

# 调用方
def main():
    calc_average = proxy_gen()
    next(calc_average)            # 预激下生成器
    print(calc_average.send(10))  # 打印：10.0
    print(calc_average.send(20))  # 打印：15.0
    print(calc_average.send(30))  # 打印：20.0

if __name__ == '__main__':
    main()