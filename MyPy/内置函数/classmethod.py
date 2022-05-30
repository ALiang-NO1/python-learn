class A(object):
    ba = 'ba'

    def func1(self):
        print('func1')

    @classmethod
    def fun2(cls):
        print('func2')
        print(cls.ba)
        cls().func1()

A.fun2()
print(getattr(A, 'ba', '错误！'))