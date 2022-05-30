from types import MethodType

class Student:
    __slots__ = ('name', 'age', 'read')  # 允许类绑定的属性

s = Student()
def read(self):
    print(self, 'is studying hard.')
s.read = MethodType(read, s)  # 给实例绑定一个方法
s.read()

Student.read = MethodType(read, Student)  # 给类绑定一个函数
s2 = Student()
s2.read()