from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
x = list(range(1, 9))
y = [3, 1, 4, 5, 8, 9, 9, 2]
plt.barh(x, y, align='center', color='c', tick_label='q a c e r j b p'.split(), hatch='\\')
plt.xlabel("箱子重量(kg)")
plt.ylabel("箱子编号(kg)")
plt.show()
