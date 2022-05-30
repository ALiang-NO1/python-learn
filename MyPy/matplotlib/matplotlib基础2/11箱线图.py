import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.random.randn(1000)
plt.boxplot(x)
plt.xticks([1], ['随机数生成AlphaRM'])
plt.grid(axis='y', ls=':', lw=1, c='gray', alpha=.4)
plt.show()
