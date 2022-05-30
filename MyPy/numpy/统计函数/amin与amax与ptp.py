import numpy as np

arr = np.arange(12).reshape(3, 4)
print("原来的数组")
print(arr)
print("沿着横轴的最小值")
print(np.amin(arr, axis=1))
print("沿着竖轴的最大值")
print(np.amax(arr, axis=0))
print("沿着横轴的最小值与最大值的差")
print(np.ptp(arr, axis=1))
