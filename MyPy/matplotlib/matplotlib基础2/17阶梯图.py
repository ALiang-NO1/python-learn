import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.linspace(1, 10, 10)
y = np.sin(x)
plt.step(x, y, color='#8dd3c7', where='post', lw=2)
plt.xlim(0, 11)
plt.xticks(np.arange(1, 11, 1))
plt.ylim(-1.2, 1.2)
plt.show()
