import numpy as np

arr = np.arange(1, 5)
print("给数组中的每个元素平方")
print(np.power(arr, 2))

print("\n给数组中的每个元素取倒")
list = np.reciprocal(arr, dtype=np.float_)
for i in list:
    print(i)