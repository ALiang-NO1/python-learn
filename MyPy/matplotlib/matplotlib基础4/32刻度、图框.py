import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
group = ['0%(Control', '1%', '5%', '15%']
# 设置绘图顺序
fig = plt.figure(figsize=(4, 3), dpi=100)
x = np.arange(11)
y = np.exp(x)
plt.plot(x, y, label='label1')

plt.xlabel('Time(d)', fontsize=14)
plt.ylabel('value', fontsize=14)
# 刻度范围
plt.xlim(-1, 20)
plt.ylim(-2, 90)
# 刻度
plt.xticks(np.linspace(0, 20, 11, endpoint=True), fontsize=10)
plt.yticks(np.linspace(0, 90, 10, endpoint=False), fontsize=10)
# 删除左边和顶部绘图区域边框线
ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
# 添加图例
plt.legend(loc='upper left', facecolor='none', edgecolor='none')
plt.show()
