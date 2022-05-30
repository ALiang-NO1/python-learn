import numpy as np

arr = np.arange(12).reshape(3, 4)
weight = np.array([[2, 2, 2, 2], [1, 2, 1, 2], [1, 1, 1, 1]])
print("arr:")
print(arr)
print()
a = np.average(arr, 1, weight, returned=True)
print(a, end='\n')