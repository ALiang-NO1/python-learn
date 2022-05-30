import numpy as np

print("-----add------")
a = np.char.add('a', 'liang')
print(a)

arr1 = ['2', 'a', 'sh']
arr2 = ['3', 'b', 'eng']
b = np.char.add(arr1, arr2)
print(b); print()

print("-----multiple------")
arr3 = [2, 3, 'a', '2']
print(np.char.multiply(arr3, 3))