from matplotlib import pyplot as plt
from matplotlib import rcParams

rcParams['font.sans-serif'] = ['SimHei']
rcParams['axes.unicode_minus'] = False
labels = list(i + '难度水平' for i in 'A B C D'.split())
students = [.35, .15, .20, .30]
colors = ["#377eb8", "#4daf4a", "#984ea3", "#ff7f00"]
explode = (0.1, 0.1, 0.1, 0.1)
plt.pie(students, explode=explode, labels=labels, autopct='%3.1f%%', startangle=45, shadow=True, colors=colors)
plt.title('选择不同难度试卷的学生百分比')
plt.show()
