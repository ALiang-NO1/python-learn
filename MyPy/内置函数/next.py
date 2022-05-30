a = filter(lambda x: x ** 2, [1, 2, 3, 4, 5])
while True:
    try:
        print(next(a))
    except StopIteration:
        break