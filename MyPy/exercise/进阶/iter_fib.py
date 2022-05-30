class Fib:
    def __init__(self):
        self.a, self.b = 0, 1

    def __iter__(self):  # Fib() 是一个迭代器，类本身就是迭代对象
        return self

    def __next__(self):
        self.a, self.b = self.b, self.a + self.b
        if self.a > 100:
            raise StopIteration()
        return self.a
# for n in Fib():
#     print(n, end='  ')

class Fib2:
    def __getitem__(self, n):
        if isinstance(n, int):  # 如果 n 是整数，执行下面的代码
            a, b = 1, 1
            for x in range(n):
                a, b = a, a + b
            return a
        if isinstance(n, slice):  # 如果 n 是切片，执行下面的代码
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

f = Fib2()
print(f[0])
print(f[:5])