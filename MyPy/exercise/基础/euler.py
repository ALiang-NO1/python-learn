"""欧拉函数，返回一个数的公因数的个数"""
euler = 1
n = int(input('请输入一个大于2的正整数：'))
for m in range(3, n):
    for i in range(2, m//2+1):
        if m % i == 0:
            break
    else:
        euler += 1
        print(m)
print('欧拉函数x={0}处的值为{1}'.format(n, euler))
