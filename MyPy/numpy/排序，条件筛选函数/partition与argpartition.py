import numpy as np

arr = np.arange(12).reshape(3, 4)
print(np.partition(arr, 3))