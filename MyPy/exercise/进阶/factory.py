# 测试工厂模式

class Factory:
    def create_car(self, brand):
        if brand == '奔驰':
            return Benz()
        if brand == '奥迪':
            return  Aodi()
        if brand == '宝马':
            return BMV()
class Benz:
    pass
class Aodi:
    pass
class BMV:
    pass

factory = Factory()
c1 = factory.create_car('奔驰')
print(c1)