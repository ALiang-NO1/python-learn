import numpy as np

arr = np.arange(12).reshape(3, 4)
print(arr)
print(np.argmax(arr, axis=1))
print(np.argmin(arr, axis=1))