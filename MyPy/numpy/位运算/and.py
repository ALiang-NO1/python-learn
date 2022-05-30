import numpy as np

print('13 和 17 的二进制形式：')
a, b = 13, 17
print(bin(a))
print(bin(b))
print()

print('13 和 17 的位与：')
c = np.bitwise_and(13, 17)
print(bin(c))