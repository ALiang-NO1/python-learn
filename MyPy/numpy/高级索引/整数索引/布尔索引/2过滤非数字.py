import numpy as np

a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a)
print(a[~np.isnan(a)])  # ~（取补运算符）来过滤 NaN