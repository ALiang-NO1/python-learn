from random import *

print("-------随机整数（闭区间）-------")
print(randint(2, 40))

print("-------随机浮点数-------")
print(uniform(1, 5))    # 在指定范围内随机生成一个浮点数
print(uniform(5, 3))    # 如果a > b，则生成的随机数n: b <= n <= a

print("-------随机抽样（样本，数量）-------")
li = [2, 4, 6, 8, 5, 3]
l = {2, 5, 8, 9, 0, 4}
print(sample(li, 4))
print(sample(l, 3))

print("-------随机数-------")
print(randrange(3, 27, 3))

print("-------随机返回一个元素-------")
strlist = ['C++', 'C#', 'Java', 'Python']
strtemp = 'Do you love python'
print(choice(strlist))
print(choice(strtemp))

print("-------打乱顺序-------")
lst = ['A', 'B', 'C', 'D', 'E']
shuffle(lst)
print(lst)

print("-------区间内随机小数-------")
print(uniform(1, 5))

print("-------比特随机数-------")
print(getrandbits(2))