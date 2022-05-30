# filter是一个过lu器
f1 = filter(lambda x: x % 2, [1, 2, 3, 4, 3])
print(list(f1))

f2 = filter(lambda x: x % 2, [1, 2, 3, 4, 4])
print(set(f2))

f3 = filter(None, 'abcd')
print(tuple(f3))

f4 = filter(lambda x: x < 5, [1, 3, 5, 6])
print(list(f4))