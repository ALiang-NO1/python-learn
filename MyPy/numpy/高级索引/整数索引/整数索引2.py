import numpy as np

x = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8], [9, 10, 11]])
print('我们的数组是：')
print(x)
rows = np.array([[0, 0], [3, 3]])   # 获取了 4X3 数组中的四个角的元素。行索引是 [0,0] 和 [3,3]
cols = np.array([[0, 2], [0, 2]])   # 而列索引是 [0,2] 和 [0,2]
y = x[rows, cols]
print('这个数组的四个角元素是：')
print(y)