import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.linspace(-1 * np.pi, 2 * np.pi)
y = np.sin(x)
plt.subplot(211)
plt.plot(x, y)
plt.subplot(212)
plt.xlim(-2 * np.pi, 2 * np.pi)
plt.xticks([-2 * np.pi, -3 * np.pi / 2, -1 * np.pi, -np.pi / 2, 0, np.pi / 2, np.pi, 3 * np.pi / 2, 2 * np.pi],
           [r'$-2\pi$', r'$-3\pi/2$', r'$-\pi$', r'$-\pi/2$', r'$0$', r'$\pi/2$', r'$\pi$', r'$3\pi/2$', r'$2\pi$'])
plt.plot(x, y)
plt.show()
