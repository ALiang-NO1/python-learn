import numpy as np
from matplotlib import cm
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
a = np.random.randn(100)
b = np.random.randn(100)
plt.scatter(a, b, s=np.power(10 * a + 20 * b, 2), c=np.random.rand(100), cmap=cm.RdYlBu, marker='o')
plt.show()
