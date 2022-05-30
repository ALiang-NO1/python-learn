import numpy as np

a = np.array([[1, 2, 3], [4, 5, 6]])

print('第一个数组：')
print(a)
print()

print('第一个数组的形状：')
print(a.shape)
print()
b = np.resize(a, (3, 2))

print('第二个数组：')
print(b)
print()

print('第二个数组的形状：')
print(b.shape)
print()
# 要注意 a 的第一行在 b 中重复出现，因为尺寸变大了

print('修改第二个数组的大小：')
b = np.resize(a, (3, 3))
print(b)