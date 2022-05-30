import numpy as np

a = np.array([[1, 2], [3, 4], [5, 6]])

print('第一个数组：')
print(a)
print()

print('未传递 Axis 参数。 在插入之前输入数组会被展开。')
print(np.insert(a, 3, [11, 12]))
print()

print('传递了 Axis 参数。 会广播值数组来配输入数组。')
print('沿轴 0 广播：')
print(np.insert(a, 1, [11], axis=0))
print()

print('沿轴 1 广播：')
print(np.insert(a, 1, 11, axis=1))