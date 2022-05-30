"""特殊方法重载"""

class Person:
    def __init__(self, name):
        self.name = name

    def __add__(self, other):
        if isinstance(other, Person):
            return '{0}--{1}'.format(self.name, other.name)
        else:
            return '不是同一类对象，不能相加！'

p1 = Person('晾')
p2 = Person('雪')
print(p1+p2)