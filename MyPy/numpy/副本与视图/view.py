import numpy as np

arr1 = np.array([3, 35, 5, 5, 26, 7])
arr2 = arr1.view()
print("修改前的arr2")
print(arr2)
arr2[0] = 100
print("修改后")
print('arr2', arr2)
print('arr1', arr1)
print("arr1的id:", id(arr1))
print("arr2的id:", id(arr2))