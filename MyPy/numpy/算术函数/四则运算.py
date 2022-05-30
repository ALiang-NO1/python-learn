import numpy as np

a = np.arange(9, dtype=np.float_).reshape(3, 3)
b = np.array([10, 10, 10])
print("原数组：", "a:", a, "b\n", b)
print("\n加法：", np.add(a, b))
print("\n减法：", np.subtract(a, b))
print("\n乘法：", np.multiply(a, b))
print("\n除法：", np.divide(a, b))