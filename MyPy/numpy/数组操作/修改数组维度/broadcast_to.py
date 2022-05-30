import numpy as np

a = np.arange(4).reshape(1, 4)

print('原数组：')
print(a)
print()

print('调用 broadcast_to 函数之后：')
print(np.broadcast_to(a, (4, 4)))