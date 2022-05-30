import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.arange(5)
y = [100, 68, 79, 91, 82]
std_err = [7, 2, 6, 10, 5]
err_attri = dict(elinewidth=2, ecolor='black', capsize=3)
plt.bar(x, y, color='c', width=.6, align='center', yerr=std_err, error_kw=err_attri,
        tick_label=list('园区' + str(i) for i in range(1, 6)))
plt.xlabel('芒果种植区')
plt.ylabel('收割量')
plt.grid(True, axis='y', ls=':', color='gray', alpha=.4)
plt.show()
