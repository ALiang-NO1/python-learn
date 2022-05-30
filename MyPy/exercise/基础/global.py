# 测试global,nonlocal关键字的用法

a = 100
b = 0


def outer():
    b = 10

    def innr():
        nonlocal b
        print('b:', b)
        b = 30
        global a
        a = 1000

    innr()
    print('outer b:', b)


outer()
print('a:', a)
