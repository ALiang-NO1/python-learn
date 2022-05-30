# 测试mro规则

class A1:
    def say(self):
        print('AAA')

class B1:
    def say(self):
        print('BBB')

class C1(A1, B1):
    def say(self):
        print('CCC')

c = C1()
print(C1.mro())   # 或者C1.__mro__
c.say()

# 继承父类方法

class A2:
    def fun(self):
        print('A2', self)
class B2(A2):
    def fun(self):
        super().fun()
        print('B2', self)
B2().fun()