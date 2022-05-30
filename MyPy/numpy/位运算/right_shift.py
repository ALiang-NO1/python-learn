import numpy as np

print('将 10 右移两位：')
a = np.right_shift(10, 2)
print(a)
print(np.binary_repr(10, width=8))
print(np.binary_repr(a, width=8))