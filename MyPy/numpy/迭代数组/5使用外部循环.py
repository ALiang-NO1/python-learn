import numpy as np

a = np.arange(0, 60, 5)
a = a.reshape(3, 4)
print('原始数组是：')
print(a)
print('\n修改后的数组是：')
for x in np.nditer(a, flags=['external_loop'], order='F'):  # 迭代器遍历对应于每列，并组合为一维数组
    print(x, end=", ")

"""c_index	可以跟踪 C 顺序的索引
f_index	    可以跟踪 Fortran 顺序的索引
multi-index	每次迭代可以跟踪一种索引类型
external_loop	给出的值是具有多个值的一维数组，而不是零维数组"""
