import numpy as np

arr = np.array([0, 30, 60, 90, 135, 180])
sin = np.sin(arr*np.pi/180, dtype=np.float_).reshape(2, 3)
print("使用sin()的结果：\n", sin)

arr1 = np.array([])
sin = np.arcsin(arr1*np.pi/180, dtype=np.float_).reshape(2, 3)
print("\n使用arcsin()的结果：\n", sin)
print(np.degrees(arr1))