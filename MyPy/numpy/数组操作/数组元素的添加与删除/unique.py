import numpy as np

a = np.array([5, 2, 6, 2, 7, 5, 6, 8, 2, 9])

print('第一个数组：')
print(a)
print()

print('第一个数组的去重值：')
u = np.unique(a)
print(u)
print()

print('去重数组的索引数组：')
u, indices = np.unique(a, return_index=True)
print(indices)
print()

print('我们可以看到每个和原数组下标对应的数值：')
print(u)
print()

print('去重数组的下标：')
u, indices = np.unique(a, return_inverse=True)
print(u)
print()

print('下标为：')
print(indices)
print()

print('使用下标重构原数组：')
print(u[indices])
print()

print('返回去重元素的重复数量：')
u, indices = np.unique(a, return_counts=True)
print(u)
print(indices)