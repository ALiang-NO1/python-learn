def fun(self, name='world'):
    print('Hello', name)

Hello = type('Hello', (object,), dict(hello=fun))  # 类名 父类元组 绑定到类方法的函数
h = Hello()
h.hello()