import numpy as np

x = np.array([[1, 2], [3, 4], [5, 6]])
y = x[[0, 1, 2], [0, 1, 0]]     # 获取数组中(0,0)，(1,1)和(2,0)位置处的元素。
print(x, '\n')
print(y)