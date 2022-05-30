from abc import ABCMeta

"""
开发一个安装程序向导，先储存做出的选择，然后点击Finish选项调用execute()方法开始安装
"""


class Wizard:
    def __init__(self, src, rootdir):
        self.choices = []
        self.src = src
        self.rootdir = rootdir

    def preferences(self, command):
        self.choices.append(command)

    def execute(self):
        for choice in self.choices:
            if list(choice.values())[0]:
                print('Copying binaries --', self.src, 'to', self.rootdir)
            else:
                print('No Option!')


if __name__ == '__main__':
    widzard = Wizard('python3.5.gzip', 'C:/user/bin/')
    widzard.preferences({'python': True})
    widzard.preferences({'java': False})
    widzard.execute()


class Command(metaclass=ABCMeta):  # 声明执行操作的接口
    def __init__(self, recv):
        self.recv = recv

    def execute(self):
        pass


class Receiver:  # 知道如何实施与执行一个请求相关的操作。
    def action(self):
        print('Receiver Action!')


class ConcreteCommand(Command):  # 将一个Receiver对象和一个操作绑定在一起。
    def __init__(self, recv):
        super().__init__(recv)

    def execute(self):
        self.recv.action()


class Invoker:  # 要求该ConcreteCommand执行这个请求。
    def command(self, cmd):
        self.cmd = cmd

    def execute(self):
        self.cmd.execute()


if __name__ == '__main__':  # 创建ConcreteCommand对象并设定其接收者。
    recv = Receiver()
    cmd = ConcreteCommand(recv)
    invoker = Invoker()
    invoker.command(cmd)
    invoker.execute()
