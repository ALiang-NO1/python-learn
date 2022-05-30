import numpy as np

a = np.arange(12).reshape(3, 4)

print('第一个数组：')
print(a)
print()

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.delete(a, 5))
print()

print('删除第二列：')
print(np.delete(a, 1, axis=1))
print()

print('包含从数组中删除的替代值的切片：')
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(np.delete(a, np.s_[::2]))