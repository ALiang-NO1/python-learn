for n in range(1, 10):
    for m in range(1, n + 1):
        print("{0}*{1}={2}".format(n, m, n * m), end='\t')
    print()
