def count():
    l = []
    for i in range(1, 4):
        def f():
            return i*i
        l.append(f())
    return l
f1, f2, f3 = count()
print(f1, f2, f3)

# 返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量
# def count():
#     def f(j):
#         def g():
#             return j*j
#         return g
#     l = []
#     for i in range(1, 4):
#         l.append(f(i))
#     return l