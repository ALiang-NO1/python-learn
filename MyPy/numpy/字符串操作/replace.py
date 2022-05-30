import numpy as np

arr = np.array(['aa', 'bb', '11', 'dd', '11'])
print(np.char.replace(arr, '11', 'll'))

print("替换二维数组中的元素")
a = np.array([['liang', 'li', 'wang'], ['hua', 'wang', 'shi']])
print(np.char.replace(a, 'wang', 'wang si le ma'))