from matplotlib import pyplot as plt
import matplotlib.font_manager

plt.axhline(y=2.0, c="r", ls="--", lw=2)
plt.axvline(x=4.0, c="b", ls="-", lw=3)

font_zh = matplotlib.font_manager.FontProperties(fname="C:\Windows\Fonts\msyhl.ttc")

plt.title("绘制参考线", fontproperties=font_zh)
plt.show()
