import matplotlib.font_manager
import numpy as np
from matplotlib import pyplot as plt

font_zh = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msyhl.ttc")
plt.title("添加注释", fontproperties=font_zh)
plt.xlim(0, 5)
plt.ylim(0, 10)
plt.annotate("注释", xy=(2, 5), xytext=(2.3, 5.2), weight='bold', fontproperties=font_zh,
             color='b', arrowprops=dict(arrowstyle='->', connectionstyle='arc3', color='b'))
plt.text(1, 9, "无指向的注释", fontproperties=font_zh)
plt.show()
