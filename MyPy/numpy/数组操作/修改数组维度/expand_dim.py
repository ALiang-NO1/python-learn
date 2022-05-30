import numpy as np

x = np.array(([1, 2], [3, 4]))
print('数组 x：')
print(x)

y = np.expand_dims(x, axis=0)
print('数组 y：')
print(y)

print('数组 x 和 y 的形状：')
print(x.shape, y.shape)
print()

# 在位置 1 插入轴
y = np.expand_dims(x, axis=1)
print('在位置 1 插入轴之后的数组 y：')
print(y)

print('x.ndim 和 y.ndim：')
print(x.ndim, y.ndim)

print('x.shape 和 y.shape：')
print(x.shape, y.shape)