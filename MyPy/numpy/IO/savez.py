import numpy as np

file = 'arrz.npy'
arr = np.arange(15).reshape(3, 5)
print(np.savez(file, arr, {arr: 'aa'}))
print(np.load(file))