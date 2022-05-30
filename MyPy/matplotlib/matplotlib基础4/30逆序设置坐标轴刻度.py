import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
time = np.arange(1, 11, .5)
machinePower = np.power(time, 2) + .7
plt.plot(time, machinePower, linestyle="-", linewidth=2, color="r")
plt.xlim(10, 1)
plt.xlabel('使用年限')
plt.ylabel('机器损耗率')
plt.title('机器损耗曲线')
plt.grid(ls=':', lw=1, color='gray', alpha=.5)
plt.show()
