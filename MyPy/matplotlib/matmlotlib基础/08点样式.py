import numpy as np
from matplotlib import pyplot as plt

# 测试不同的点样式
# rng = np.random.RandomState(0)
# for marker in 'o . , X + ^ v < > s d'.split():
#     plt.plot(rng.rand(5), rng.rand(5), marker+'-', label='marker=%s' % marker)

# 测试缩写含义
x = np.array([1, 8])
y = np.array([3, 10])
plt.plot(x, y, 'o', ms=20, mec='k', ls='--', c='c', lw=4)  # markersize markerfacecolor

plt.legend()
plt.xlim(0)  # 坐标原点在角上，没有距离
plt.show()
