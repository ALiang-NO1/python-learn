"""1.工厂模式是一个在软件开发中用来创建对象的设计模式。
2.工厂模式包涵一个超类。这个超类提供一个抽象化的接口来创建一个特定类型的对象，而不是决定哪个对象可以被创建。
3.为了实现此方法，需要创建一个工厂类创建并返回。
4.当程序运行输入一个“类型”的时候，需要创建于此相应的对象。这就用到了工厂模式。在如此情形中，实现代码基于工厂模式，可以达到可扩展，可维护的代码。
当增加一个新的类型，不在需要修改已存在的类，只增加能够产生新类型的子类。"""

class Person:
    def __init__(self):
        self.name = None
        self.gender = None

    def getName(self):
        return self.name

    def getGender(self):
        return self.gender

class Male(Person):
    def __init__(self, name):
        print("Hello Mr." + name)

class Female(Person):
    def __init__(self, name):
        print("Hello Miss." + name)

class Factory:
    def getPerson(self, name, gender):
        if gender == 'M':
            return Male(name)
        if gender == 'F':
            return Female(name)


if __name__ == '__main__':
    factory = Factory()
    person = factory.getPerson("Chetan", "M")