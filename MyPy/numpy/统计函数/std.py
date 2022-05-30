import numpy as np

arr = np.arange(12).reshape(3, 4)
print("arr")
print(arr)
print("标准差")
print(np.std(arr, axis=1))
print("方差")
print(np.var(arr, axis=1))