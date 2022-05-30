# 测试类方法

class Student:
    company = 'ccdx'

    @classmethod
    def printCompany(cls, adress, year):
        cls.adress = adress
        cls.year = year
        print(cls.company, cls.adress, cls.year)

Student.printCompany('JiLin', 16)