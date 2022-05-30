"""
电脑有关、开、睡眠、挂起四个状态，不同状态有不同操作
"""


class ComputeState:
    name = 'state'
    allowed = []

    def switch(self, state):
        if state.name in self.allowed:
            print('Current:', self, '=> switched to new state', state)
            self.__class__ = state  # __class__是每个类的内部属性，表示对类的引用
        else:
            print('Current:', self, '=> switched to', state.name, 'not possible!')

    def __str__(self):
        return self.name


class Off(ComputeState):
    name = 'off'
    allowed = ['on']


class On(ComputeState):
    name = 'on'
    allowed = ['off', 'suspend', 'hibernate']


class Suspend(ComputeState):
    name = 'suspend'
    allowed = ['on']


class Hibernate(ComputeState):
    name = 'hibernate'
    allowed = ['on']


class Computer:
    def __init__(self, model='HP'):
        self.model = model
        self.state = Off()

    def change(self, state):
        self.state.switch(state)


if __name__ == '__main__':
    comp = Computer()
    comp.change(On)
    comp.change(Off)
    comp.change(On)
    comp.change(Suspend)
    comp.change(Hibernate)
