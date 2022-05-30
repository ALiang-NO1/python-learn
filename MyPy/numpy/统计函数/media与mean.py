import numpy as np

arr = np.array([[3, 5, 7, 6], [3, 8, 3, 5], [0, 5, 5, 8]])
print("横着求中位数")
print(np.median(arr, axis=1))
print("竖着求平均数")
print(np.mean(arr, axis=1))