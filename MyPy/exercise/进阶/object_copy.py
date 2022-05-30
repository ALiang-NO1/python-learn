# 对象的深浅拷贝

import copy

class MobilePhone:
    def __init__(self, cpu, screen):
        self.cpu = cpu
        self.screen = screen

class CPU:
    def calaulate(self):
        pass

class Screen:
    def show(self):
        pass

s1 = CPU()
s2 = Screen()
m1 = MobilePhone(s1, s2)
m2 = copy.copy(m1)
print(m1, m1.cpu, m1.screen)
print(m2, m2.cpu, m2.screen)
