from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
kinds = "简易箱 保温箱 行李箱 密封箱".split()
colors = ["#e41a1c", "#377eb8", "#4daf4a", "#984ea3"]
soldNums = [0.05, 0.45, 0.15, 0.35]
plt.pie(soldNums, labels=kinds, autopct='%3.1f%%', startangle=60, colors=colors)
plt.title("不同箱子的销售数量占比")
plt.show()
