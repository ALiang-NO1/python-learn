from numpy import matlib as mt
import numpy as np

print("eye")
print(mt.eye(3, 5, 0, int))
print("identify")
print(mt.identity(5, int))
print("rand随机填充")
print(mt.rand(3, 5))
print("转二维")
i = np.matrix('1,2;3,4')
print('i')
print(i)
j = np.asarray(i)
print('j')
print(j)
k = np.asmatrix(j)
print('k')
print(k)