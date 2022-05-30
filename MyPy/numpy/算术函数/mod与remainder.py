import numpy as np

arr1 = np.arange(6, 15).reshape(3, 3)
arr2 = np.arange(10, 19).reshape(3, 3)
print("mod:\n", np.mod(arr2, arr1))
print("\nremainder:\n", np.remainder(arr2, arr1))