"""抽象方法表示基类的一个方法，没有实现，所以基类不能实例化，子类实现了该抽象方法才能被实例化。
Python的abc提供了@abstractmethod装饰器实现抽象方法

在Python3.4中，声明抽象基类最简单的方式是子类话abc.ABC；
Python3.0到Python3.3，必须在class语句中使用metaclass=ABCMeta；Python2中使用__metaclass__=ABCMeta
"""

from abc import abstractmethod, ABCMeta, ABC

class Foo(metaclass=ABCMeta):
    @abstractmethod
    def fun(self):
        pass

class SubA(Foo):
    def fun(self):
        print("SubA.fun()")

# a = Foo()    # error
b = SubA()
b.fun()

class Foo2(ABC):
    @abstractmethod
    def fun2(self):
        """please implemente in subclass"""

class SubA2(Foo):
    def fun(self):
        print('SubA2.fun()')

b2 = SubA2()
b2.fun()
a2 = Foo2()   # error
