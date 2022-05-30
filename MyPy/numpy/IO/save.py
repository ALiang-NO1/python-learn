import numpy as np

file = 'arr.npy'
arr = np.arange(15).reshape(3, 5)
print(np.save(file, arr, allow_pickle=True, fix_imports=True))
print(np.load(file))