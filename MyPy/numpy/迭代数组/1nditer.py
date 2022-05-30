import numpy as np

a = np.arange(6).reshape(2, 3)
print('原始数组是：')
print(a)
print('迭代输出元素：')
for x in np.nditer(a):  # 选择的顺序是和数组内存布局一致
    print(x, end=", ")