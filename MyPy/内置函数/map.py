m1 = map(lambda x: x*2, [1, 2, 3])
print('m1:', list(m1))

m2 = map(lambda x, y: x+y, [1, 2, 3], [6, 6, 6])
print('m2:', list(m2))

m3 = map(lambda x: x*2, [1, 2, 3])
print('m3:', list(m3))

m4 = map(lambda x, y: x+y, ['a', 'ab', 'cd'], ['q'])
print('m4:', list(m4))

def f(x, y):
    return x+y
l1 = [0, 1, 2, 3, 4]
l2 = ['0', 'a', 'b', 'c', 'd']
l3 = map(f, l1, l2)
print(list(l3))
f(l1, l2)