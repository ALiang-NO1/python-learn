def fun(n):
    n = int(n)
    assert n != 0, 'n can`t be 0'
    return 10/n
print(fun(0))