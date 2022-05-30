import numpy as np

print("用#填充单个字符串")
print(np.char.center('aaaa', 8, '#'))
print("填充字符串数组")
arr = np.array([['xiang'], ['ni'], ['le']])
print(np.char.center(arr, 8, '*'))