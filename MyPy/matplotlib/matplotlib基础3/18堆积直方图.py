import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
scoreT1 = np.random.randint(0, 100, 100)
scoreT2 = np.random.randint(0, 100, 100)
x = [scoreT1, scoreT2]
colors = ['#8dd3c7', '#bebada']
labels = ['班级A', '班级B']
bins = range(0, 101, 10)
plt.hist(x, bins=bins, color=colors, histtype='bar', rwidth=10, stacked=True, label=labels)
plt.xlabel('测试成绩')
plt.xlabel('学生人数')
plt.title('不同班级成绩直方图')
plt.legend(loc='upper left')
plt.show()
