"""
测试property装饰器: 把方法变成属性调用
@property 广泛应用在类的定义中，可以让调用者写出简短的代码，
同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。
"""

class Employee:

    @property    # @property修饰的属性，默认只读
    def salary(self):
        return self._salary

    # @salary.getter
    # def salary(self):
    #     return self._salary

    # 近代人做法
    # def set_salary(self, value):
    #     if not isinstance(value, int):
    #         raise ValueError('参数错误，必须为整数')
    #     if value < 1000 or value > 50000:
    #         raise ValueError('参数错误，必须介于1000~5000')
    #     self._salary = value

    # 现代人做法
    @salary.setter
    def salary(self, value):
        if not isinstance(value, int):
            raise ValueError('参数错误，必须为整数')
        if value < 2000 or value > 50000:
            raise ValueError('参数错误，必须介于1000~5000')
        self._salary = value

emp = Employee()
# emp.set_salary(100)
emp.salary = 100
print(emp.salary)