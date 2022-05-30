"""
为每一个新注册的博客用户发送邮件信息，注册值不高也发送信息
"""
class Subject:
    def __init__(self):
        self.__observers = []

    def register(self, observer):
        self.__observers.append(observer)

    def notifyAll(self, *args, **kwargs):
        for observer in self.__observers:
            observer.notify(self, *args, **kwargs)


class Observer:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ': Got', args, 'From', subject)


class Observer2:
    def __init__(self, subject):
        subject.register(self)

    def notify(self, subject, *args):
        print(type(self).__name__, ': Got', args, 'From', subject)


subject = Subject()
observer = Observer(subject)
observer2 = Observer(subject)
subject.notifyAll('notification')
