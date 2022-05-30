import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.arange(5)
y1 = [100, 68, 79, 91, 82]
y2 = [120, 75, 70, 78, 85]
std_err1 = [7, 2, 6, 10, 5]
std_err2 = [5, 1, 4, 8, 9]
error_attri = dict(elinewidth=2, ecolor='black', capsize=3)
bar_width = .4
tick_label = list('园区' + str(i) for i in range(1, 6))
plt.bar(x, y1, bar_width, color='#87ceeb', align='center', yerr=std_err1, error_kw=error_attri, label='2010')
plt.bar(x + bar_width, y2, bar_width, color='#cd5c5c', align='center', yerr=std_err2, error_kw=error_attri,
        label='2013')
plt.xlabel('芒果种植区')
plt.ylabel('收割量')
plt.xticks(x + bar_width / 2, tick_label)
plt.title('不同年份芒果种植区单次收割量')
plt.grid(True, axis='y', ls=':', color='gray', alpha=.4)
plt.legend()
plt.show()
