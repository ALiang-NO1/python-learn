import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：')
print(a)
print()

print('向数组添加元素：')
print(np.append(a, [7, 8, 9]))
print()

print('沿轴 0 添加元素：')
print(np.append(a, [[7, 8, 9]], axis=0))
print()

print('沿轴 1 添加元素：')
print(np.append(a, [[5, 5, 5], [7, 8, 9]], axis=1))