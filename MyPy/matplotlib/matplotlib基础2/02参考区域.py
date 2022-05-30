import matplotlib.font_manager
from matplotlib import pyplot as plt

plt.xlim(0, 5)
plt.ylim(0, 10)
plt.axvspan(xmin=3.0, xmax=4.0, facecolor='grey', alpha=.3)
plt.axhspan(ymin=4.0, ymax=6.0, facecolor='y', alpha=.3)

font_zh = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msyhl.ttc")
plt.title("绘制参考区域", fontproperties=font_zh)
plt.show()
