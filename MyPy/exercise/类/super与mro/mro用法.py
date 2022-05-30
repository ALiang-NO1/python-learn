# super(type, obj) 类  该类对象
"""super().fun = super(B, self).fun() = super(__class__, self).fun()"""

class A:
    def fun(self):
        print('A.fun')

class B:
    def fun(self):
        print('B.fun')

class C:
    def fun(self):
        print('C.fun')

class D(A, B):
    def fun(self):
        print('AB.fun')

class E(B, C):
    def fun(self):
        print('BC.fun')

class F(D, E):
    def fun(self):
        print('DE.fun')

super(E, F()).fun()
super(D, F()).fun()

# super(type1, type2)  type2是type1的子类
print("------用法2--------")
print(super(F, F()))
print(super(F, F))
print(super(E, F))
print(super(F, F()).fun())
print(super(E, F).fun())
