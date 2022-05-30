import numpy as np

arr = np.array([12.3546, 23.35436, 35.354])
print("\n原数组：", arr)
print("\n保留两位小数：", np.around(arr, decimals=2))
print("\n保留-1位小数：", np.around(arr, decimals=-1))