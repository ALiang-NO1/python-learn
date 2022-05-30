import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = np.arange(5)
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]
bar_width = .35
tick_label = list('A B C D E'.split())
plt.bar(x, y, bar_width, color='c', align='center', label='班级A', alpha=.5)
plt.bar(x + bar_width, y1, bar_width, color='b', align='center', label='班级B', alpha=.5)
plt.xlabel('测试难度')
plt.ylabel('试卷份数')
plt.xticks(x + bar_width / 2, tick_label)
plt.legend()
plt.show()
