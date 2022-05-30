def fun(x):
    return x ** 2 + x -1
def newton(a,b,e):
    x = (a + b)/2.0
    if abs(b-a) < e:
        return x
    else:
        if fun(a) * fun(x) < 0:
            return newton(a, x, e)
        else:
            return newton(x, b, e)
print(newton(-5, 0, 5e-5))