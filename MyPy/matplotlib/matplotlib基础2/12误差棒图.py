import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.linspace(.1, .6, 6)
y = np.exp(x)
plt.errorbar(x, y, fmt='bo:', yerr=.2, xerr=.02)
plt.xlim(0, .7)
plt.show()
