from abc import ABCMeta, abstractmethod

"""
收音机有两种频率：AM和FM，切换AM按钮时频率改为AM，切换FM按钮频率改为FM
"""


class State(metaclass=ABCMeta):
    @abstractmethod
    def handle(self):
        pass


class ConcreteStateA(State):  # 根据状态变化采取相应措施
    def handle(self):
        print('ConcreteStateA')


class ConcreteStateB(State):
    def handle(self):
        print('ConcreteStateB')


class Context(State):  # 接收客户端请求，维护对象状态引用
    def __init__(self):
        self.state = None

    def getState(self):
        return self.state

    def setState(self, state):
        self.state = state

    def handle(self):
        self.state.handle()


context = Context()
stateA = ConcreteStateA()
stateB = ConcreteStateB()
context.setState(stateA)
context.handle()
context.setState(stateB)
context.handle()
