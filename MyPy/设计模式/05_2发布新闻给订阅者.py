"""
订户可以通过报纸、邮箱、短信、语音等方式获取新闻机构发布的消息，用观察者模式实现新闻发布
"""
from abc import ABCMeta, abstractmethod


class NewsPublisher:
    def __init__(self):
        self.__subscribers = []
        self.__latestNews = None

    def attach(self, subscriber):
        self.__subscribers.append(subscriber)

    def detatch(self):
        self.__subscribers.pop()

    def subscribers(self):
        return [type(x).__name__ for x in self.__subscribers]

    def notifySubscribers(self):
        for sub in self.__subscribers:
            sub.update()

    def addNews(self, news):
        self.__latestNews = news

    def getNews(self):
        return 'Got news:' + self.__latestNews


class Subscribers(metaclass=ABCMeta):
    @abstractmethod
    def update(self):
        pass


class SMSSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class EmailSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


class AnyOtherSubscriber:
    def __init__(self, publisher):
        self.publisher = publisher
        self.publisher.attach(self)

    def update(self):
        print(type(self).__name__, self.publisher.getNews())


if __name__ == '__main__':
    news_publisher = NewsPublisher()
    for subscribers in [SMSSubscriber, EmailSubscriber, AnyOtherSubscriber]:
        subscribers(news_publisher)
    print('Subscribers:', news_publisher.subscribers())
    news_publisher.addNews('News!')
    news_publisher.notifySubscribers()
    print('Detatched:', type(news_publisher.detatch()).__name__)
    print('Subscribers:', news_publisher.subscribers())
    news_publisher.addNews('News2')
    news_publisher.notifySubscribers()
