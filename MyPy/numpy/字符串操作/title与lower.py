import numpy as np

print("对字符串数组中的元素首字母大写")
arr1 = np.array(['wo jiao', 'jin', 'rui', 'liang'])
print(np.char.title(arr1))

print("\n对字符串数组中的元素每个字母小写")
arr2 = np.array(['ZHONG', 'HUA', 'JUE', 'QI'])
print(np.char.lower(arr2))