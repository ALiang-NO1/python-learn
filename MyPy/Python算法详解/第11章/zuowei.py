# teachers=['a','b','c','d','e','f','g','h','j','k','m']
# offices=[[],[],[],[]]
# 要求是将11名老师随机分配到4个办公室，每个办公室保证至少分配两名老师。


import random

teachers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'm']

offices = [[], [], [], []]


class Office:
    def __init__(self, num):
        self.teachers_list = []
        self.num = num

    def add(self, x):
        self.teachers_list.append(x)

    def ret(self):
        return self.teachers_list

    def __str__(self):
        return str(self.num)


# 调用系统时间，实现随机数
random.seed()

# 一共3种情况：
# 3 3 3 2 = 11
# 4 2 3 2 = 11
# 5 2 2 2 = 11
case_index = random.randrange(1, 4)
offices_list = []
if case_index == 1:
    # 3 3 3 2
    for e in [3, 3, 3, 2]:
        offices_list.append(Office(e))
elif case_index == 2:
    # 4 2 3 2
    for e in [4, 3, 2, 2]:
        offices_list.append(Office(e))
else:
    # 5 2 2 2
    for e in [5, 2, 2, 2]:
        offices_list.append(Office(e))

# 打乱顺序
random.shuffle(offices_list)

print("办公室随机分配名额如下：")
for office in offices_list:
    print(office, end=" ")

print()
print("开始分配老师：")
# 分配老师
for teacher in teachers:
    while True:
        index = random.randrange(0, len(offices))
        office = offices_list[index]
        if len(office.teachers_list) >= office.num:
            continue
        office.add(teacher)
        break

for i in range(len(offices_list)):
    office = offices_list[i]
    offices[i] = office.ret()
    print(offices[i])