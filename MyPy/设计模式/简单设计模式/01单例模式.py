"""是一种常用的软件设计模式，该模式的主要目的是确保某一个类只有一个实例存在。当你希望在整个系统中，某个类只能出现一个实例时，单例对象就能派上用场"""

class Singleton(object):
    def __init__(self):
        pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"):     # 反射
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1 == obj2)