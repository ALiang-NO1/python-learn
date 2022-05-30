from abc import ABCMeta, abstractmethod

"""
在IOS上开发开发自己的交叉编译器并运行，先开发一个抽象类，编译器收集源码，然后编译
"""


class Compile(metaclass=ABCMeta):
    @abstractmethod
    def collectSource(self):
        pass

    @abstractmethod
    def compileToObject(self):
        pass

    @abstractmethod
    def run(self):
        pass

    def compileAndRun(self):
        self.collectSource()
        self.compileAndRun()
        self.run()


class IOSCompile(Compile):
    def collectSource(self):
        print('Collecting Swift Code.')

    def compileToObject(self):
        print('Compiling swift code to LLVM bitcode.')

    def run(self):
        print('Program running on runtime environment')


ios = IOSCompile()
ios.run()


class AbstractClass(metaclass=ABCMeta):  # 算法的操作或步骤
    def __init__(self):
        pass

    @abstractmethod
    def operation(self):
        pass

    @abstractmethod
    def operation2(self):
        pass

    @abstractmethod
    def template_method(self):  # 算法框架，定义序列或算法本身
        print('Defining the Algorithm. Operation follows operation.')
        self.operation()
        self.operation2()


class ConcreteClass(AbstractClass):  # 执行算法子类的特定步骤
    def operation(self):
        print('My Concrete Operation.')

    def operation2(self):
        print('Operation2 remains same.')


class Client:
    def main(self):
        self.concrete = ConcreteClass()
        self.concrete.template_method()


client = Client()
client.main()
