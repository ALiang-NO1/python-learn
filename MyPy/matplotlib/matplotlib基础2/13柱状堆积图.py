from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = list(range(1, 6))
y = [6, 10, 4, 5, 1]
y1 = [2, 6, 3, 8, 5]
plt.bar(x, y, align='center', color='#66c2a5', tick_label='A B C D E'.split(), label='班级A')
plt.bar(x, y1, align='center', bottom=y, color='#8da0cb', label='班级B')
plt.xlabel('测试难度')
plt.ylabel('试卷份数')
plt.legend()
plt.show()
