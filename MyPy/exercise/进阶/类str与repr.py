class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return "我叫%s, 今年%s岁了！" % (self.name, self.age)

    # 控制台输出 s 还是返回类地址，因为控制台没有调用__str__()，而是调用__repr__()
    __repr__ = __str__  # 偷懒写法

s = Student('liang', 18)
print(s)
print(type(s))
print(type(s.age))
