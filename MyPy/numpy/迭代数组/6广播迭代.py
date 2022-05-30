import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('第一个数组为：')
print(a)
print('第二个数组为：')
b = np.array([1, 2, 3, 4], dtype=int)
print(b)
print('修改后的数组为：')
for x, y in np.nditer([a, b]):
    print("%d-%d" % (x, y), end=", ")