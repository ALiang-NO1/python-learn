from functools import reduce, partial

r1 = reduce(lambda x, y: x+y, range(10))
print('r1:', r1)

r2 = reduce(lambda x, y: x+y, ['a', 'b', 'c', 'd'], 'ee')
print('r2:', r2)

def showarg(*args, **kwargs):
    print(args)
    print(kwargs)
p1 = partial(showarg, 1, 2, 3)
p1()
p1(4, 5, 6)
p1(a='python', b='C++')

p2 = partial(showarg, a=3, b=4)