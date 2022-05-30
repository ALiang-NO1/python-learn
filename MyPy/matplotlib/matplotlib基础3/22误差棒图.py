import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.linspace(.1, .6, 10)
y = np.exp(x)
error = .05 + .15 * x
lower_error = error
upper_error = .3 * error
error_limit = [lower_error, upper_error]
plt.errorbar(x, y, yerr=error_limit, fmt=':o', ecolor='y', elinewidth=4, ms=5, mfc='c', mec='r', capthick=1, capsize=2)
plt.xlim(0, .7)
plt.show()
