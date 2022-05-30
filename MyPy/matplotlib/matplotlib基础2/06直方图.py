import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.random.randint(0, 10, 100)
bins = range(0, 11, 1)
plt.hist(x, bins=bins, color='g', histtype='bar', rwidth=1, alpha=.3)
plt.xlabel('箱子重量（kg）')
plt.ylabel('销售数量（个）')
plt.show()
