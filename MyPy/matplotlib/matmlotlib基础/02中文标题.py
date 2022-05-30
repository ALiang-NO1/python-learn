import matplotlib.font_manager
import numpy as np
from matplotlib import pyplot as plt

font_zh = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msyhl.ttc")
x = np.arange(1, 11)
y = x * 2 + 5

plt.title("中文字体测试", fontproperties=font_zh, fontsize=15)
plt.xlabel("x轴", fontproperties=font_zh)
plt.ylabel("y轴", fontproperties=font_zh)

plt.grid(axis='x', color='g', linestyle='--', linewidth=1)  # 添加横轴网格线
plt.plot(x, y)
plt.show()
