a = 100
def func(arg):
    z = 1
    print('#'*10)
    print(locals())

    print('#'*10)
    a = globals()
    # print(a)
    for value in a:
        print(value)

func(2)