class A:
    def fun():
        print('staticmethod成功!')
    staticmethod(fun)

    @staticmethod
    def fun2():
        print('静态函数fun2()运行成功')

A.fun()
A.fun2()