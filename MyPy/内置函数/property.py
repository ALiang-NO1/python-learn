"""
class property([fget[, fset[, fdel[, doc]]]])
fget -- 获取属性值的函数
fset -- 设置属性值的函数
fdel -- 删除属性值函数
doc -- 属性描述信息"""


class C(object):
    def __init__(self):
        self._x = None

    def getx(self):
        return self._x

    def setx(self, value):
        self._x = value

    def delx(self):
        del self._x
    # 如果 c 是 C 的实例化, c.x 将触发 getter,c.x = value 将触发 setter ， del c.x 触发 deleter
    x = property(getx, setx, delx, "I'm the 'x' property.")
c = C()
c.x = 100
print(c.x)
del c.x
print(c.x)