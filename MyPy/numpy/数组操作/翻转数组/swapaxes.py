import numpy as np

# 创建了三维的 ndarray
a = np.arange(8).reshape(2, 2, 2)

print('原数组：')
print(a)

# 现在交换轴 0（深度方向）到轴 2（宽度方向）
print('调用 swapaxes 函数后的数组：')
print(np.swapaxes(a, 2, 0))