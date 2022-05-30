import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print()
print('原始数组的转置是：')
b = a.T
print(b)
print()
print('以 C 风格顺序排序：')
c = b.copy(order='C')
print(c)
for x in np.nditer(c):
    print(x, end=", ")
print()
print('以 F 风格顺序排序：')
c = b.copy(order='F')
print(c)
for x in np.nditer(c):
    print(x, end=", ")