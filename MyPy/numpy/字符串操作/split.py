import numpy as np

print("用逗号分隔")
arr = np.array(['a', 'b', '3', 'c'])
print(np.char.split(arr, ','))

print("\n用\\n, \\r或\\n\\r分隔")
print(np.char.splitlines(arr))