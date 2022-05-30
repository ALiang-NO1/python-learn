import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
barSlices = 12
theta = np.linspace(.0, 2 * np.pi, barSlices, endpoint=False)
r = 30 * np.random.rand(barSlices)
plt.polar(theta, r, color='chartreuse', linewidth=2, marker='*', mfc='b', ms=10)
plt.show()
