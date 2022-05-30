from abc import ABCMeta, abstractmethod

"""
作为证券交易所用户并不直接买入或卖出，而是创建订单由代理或经纪人向证券交易所提交请求完成工作
若股市未开张则可以向经纪人提出请求，然后放入队列
"""


class Order(metaclass=ABCMeta):
    @abstractmethod
    def execute(self):
        pass


class BuyStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.buy()


class SellStockOrder(Order):
    def __init__(self, stock):
        self.stock = stock

    def execute(self):
        self.stock.sell()


class StockTrade:
    def buy(self):
        print('You will Buy stocks.')

    def sell(self):
        print('You will sell stocks.')


class Agent:
    def __init__(self):
        self.__orderQueue = []

    def placeOrder(self, order):
        self.__orderQueue.append(order)


if __name__ == '__main__':
    stock = StockTrade()
    buy = BuyStockOrder(stock)
    sell = SellStockOrder(stock)
    agent = Agent()
    agent.placeOrder(buy)
    agent.placeOrder(sell)
