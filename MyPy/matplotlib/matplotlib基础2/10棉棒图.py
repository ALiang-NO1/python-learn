import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.linspace(0.5, 2 * np.pi, 20)
y = np.random.randn(20)
plt.stem(x, y, linefmt='-.', markerfmt='o', basefmt='-')
plt.show()
