import numpy as np

a = np.arange(12).reshape(3, 4)

print('原数组：')
print(a)
print('\n')

print('对换数组：')
print(np.transpose(a))
print("用T操作结果：")
print(a.T)