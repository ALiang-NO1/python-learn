import numpy as np

a = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(a)
print(a[np.iscomplex(a)])