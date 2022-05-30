from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
labels = list(i + '水平难度' for i in 'A B C D'.split())
students = [.35, .15, .20, .30]
explode = (.1, .1, .1, .1)
colors = ["#377eb8", "#e41a1c", "#4daf4a", "#984ea3"]
plt.pie(students, explode=explode, labels=labels, autopct='%1.1f%%', startangle=45, shadow=True, colors=colors)
plt.title('选择不同难度试卷的学生百分比')
rowLabels = ['学生选择试卷人数']
strdentValues = [[350, 150, 200, 300]]
plt.table(cellText=strdentValues, cellLoc='left', colWidths=[.1] * 4, rowLabels=rowLabels, colLabels=labels,
          rowLoc='center', colColours=colors, loc='bottom')
plt.show()
