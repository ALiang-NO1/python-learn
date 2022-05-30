import matplotlib.font_manager
import numpy as np
from matplotlib import pyplot as plt

ttf_list = sorted([f.name for f in matplotlib.font_manager.fontManager.ttflist])
# for i in ttf_list:
#     print(i, end='  ')
# plt.rcParams['font.family'] = ['STFangsong']

zfont = matplotlib.font_manager.FontProperties(fname="SourceHanSansSc-Bold.otf", size=18)
font1 = {'color': 'blue', 'size': 20}
font2 = {'color': 'darked', 'size': 15}
x = np.arange(1, 11)
y = 2 * x + 5

plt.title("系统中文字体测试", fontproperties=zfont)

plt.xlabel("x轴", fontproperties=zfont, fontdict=font1)
plt.xlabel("y轴", fontproperties=zfont, fontdict=font2)
plt.plot(x, y)
plt.show()
