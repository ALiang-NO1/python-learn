import numpy as np

arr = np.random.randint(1, 20, 15).reshape(3, 5)
print(arr)
print()
print(np.sort(arr, axis=1, kind='quicksort'))
print("\n数组值从小到大值的索引")
print(np.argsort(arr))