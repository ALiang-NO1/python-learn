import numpy as np
from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
testA = np.random.randn(5000)
testB = np.random.randn(5000)
testList = [testA, testB]
labels = ['随机数生成器AlphaRMB', '随机数生成器BetaRMB']
colors = ['#1b9e77', '#d95f02']
whis = 1.6
width = .35
bplot = plt.boxplot(testList, widths=whis, sym='o', labels=labels, patch_artist=True)
for patch, color in zip(bplot['boxes'], colors):
    patch.set_facecolor(color)
plt.ylabel('随机数值')
plt.title('生成器抗干扰能力的稳定性比较')
plt.grid(axis='y', ls=':', lw=1, color='gray', alpha=.4)
plt.show()
