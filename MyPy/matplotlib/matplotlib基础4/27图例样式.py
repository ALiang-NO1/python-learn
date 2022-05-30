import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.arange(0, 2.1, .1)
y = np.power(x, 3)
y1 = np.power(x, 2)
y2 = np.power(x, 1)
plt.plot(x, y, ls='-', lw=2, label='$x^{3}$')
plt.plot(x, y1, ls='-', lw=2, c='r', label='$x^{2}$')
plt.plot(x, y2, ls='-', lw=2, c='y', label='$x^{1}$')
plt.legend(loc='upper left', bbox_to_anchor=(.05, .95), ncol=3, title='power function', shadow=True, fancybox=True)
plt.show()
