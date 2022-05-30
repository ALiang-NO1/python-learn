from matplotlib import pyplot as plt
import matplotlib.font_manager
import numpy as np

x = np.array()
y = np.array()

font_zh = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msyhl.ttc")
plt.title("绘制参考线", fontproperties=font_zh)
plt.xlabel("", fontproperties=font_zh)
plt.ylabel("", fontproperties=font_zh)
plt.plot(x, y)
plt.show()


from matplotlib import pyplot as plt
from matplotlib import rcParams
import numpy as np

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False

plt.show()