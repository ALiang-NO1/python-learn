import numpy as np

print('13 的位反转，其中 ndarray 的 dtype 是 uint8：')
print(np.invert(np.array([13], dtype=np.uint8)))
print()
# 比较 13 和 242 的二进制表示，我们发现了位的反转

print('13, 242的二进制表示：')
print(np.binary_repr(13, width=8))
print(np.binary_repr(242, width=8))
print()