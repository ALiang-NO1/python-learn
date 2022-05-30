import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.arange(5)
y1 = [1200, 2400, 1800, 2200, 1600]
y2 = [1050, 2100, 1300, 1600, 1340]
std_err1 = [150, 100, 180, 130, 80]
std_err2 = [120, 110, 170, 150, 120]
bar_width = .6
tick_label = '家庭 小说 心理 科技 儿童'.split()
error_attri = dict(elinewidth=2, ecolor='black', capsize=0)
plt.bar(x, y1, bar_width, color='#6495ed', align='center', yerr=std_err1, label='地区1', error_kw=error_attri)
plt.bar(x, y2, bar_width, color='#ffa500', align='center', yerr=std_err2, label='地区2', error_kw=error_attri)
plt.xlabel('图书种类')
plt.ylabel('订购数量')
plt.title('不同地区大型图书展销会图书采购情况')
plt.grid(True, axis='y', ls=':', color='gray', alpha=.2)
plt.xticks(x, tick_label)
plt.legend()
plt.show()
