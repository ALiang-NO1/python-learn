import numpy as np

print(np.char.join(':', 'abcd'))
print("\n用两个不同的连接符连接两个字符串")
print(np.char.join([':', '-'], ['abcd', 'efgh']))