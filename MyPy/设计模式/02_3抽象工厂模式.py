"""
印度和墨西哥披萨，都有蔬菜和非蔬菜类型，蔬菜类有服务方法，非蔬菜类型有备用方法，在蔬菜上放上火腿变成非素类
"""
from abc import ABCMeta, abstractmethod


class PizzaFactory(metaclass=ABCMeta):
    @abstractmethod
    def createVegPizza(self):
        pass

    def createNonVegPizza(self):
        pass


class IndianPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return DeluxVeggiePizza()

    def createNonVegPizza(self):
        return ChickenPizza()


class USPizzaFactory(PizzaFactory):
    def createVegPizza(self):
        return MexicanVegPizza()

    def createNonVegPizza(self):
        return HamPizza()


class VegPizza(metaclass=ABCMeta):
    @abstractmethod
    def prepare(self):
        pass


class NonVegPizza(metaclass=ABCMeta):
    @abstractmethod
    def serve(self, VegPizza):
        pass


class DeluxVeggiePizza(VegPizza):
    def prepare(self):
        print('Prepare ', type(self).__name__)


class ChickenPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, 'is served with Chicken on', type(VegPizza).__name__)


class MexicanVegPizza(VegPizza):
    def prepare(self):
        print('Prepare', type(self).__name__)


class HamPizza(NonVegPizza):
    def serve(self, VegPizza):
        print(type(self).__name__, 'is served with Ham on', type(VegPizza).__name__)


class PizzaStore:
    def makePizzas(self):
        for factory in [IndianPizzaFactory(), USPizzaFactory()]:
            self.factory = factory
            self.nonVegPizza = self.factory.createNonVegPizza()
            self.vegPizza = self.factory.createVegPizza()
            self.vegPizza.prepare()
            self.nonVegPizza.serve(self.vegPizza)


pizza = PizzaStore()
pizza.makePizzas()
