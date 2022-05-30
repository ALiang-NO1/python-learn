class Car:
    """一次模拟汽车的简单尝试"""
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 100

    def get_discriptive_name(self):
        long_name = self.year, self.make, self.model
        print(long_name)

    def read_odometer(self):
        print("This car has ", self.odometer_reading, " miles on it")

    def update_odometer_reading(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back odometer!")


class ElectricCar(Car):
    """电动车的独特之处"""
    def __init__(self, make, model, year):
        """初始化父类的属性"""
        super().__init__(make, model, year)
        self.battery_size = 70

    def describe_battery(self):
        print("This car has ", self.battery_size, "kwh battery!")

    def fill_gas_tank(self):
        """电动车没有油缸"""
        print("This car doesn't have a gase tank!")
        
mycar = Car('benchi', 'model_S', 2020)
print("汽车制造商：", mycar.make)
print("汽车全名：")
mycar.get_discriptive_name()
print("汽车里程读数：")
mycar.update_odometer_reading(98)
mycar.read_odometer()
print('----constructor a electricCar---')
ele_car = ElectricCar('small knif', 'modle_A', 2021)
ele_car.get_discriptive_name()
print(ele_car.describe_battery())
print(ele_car.fill_gas_tank())
