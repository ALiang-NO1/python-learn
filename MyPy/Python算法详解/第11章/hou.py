def fun(n):
    m = [[0] * n for i in range(n)]
    x, y = 0, n // 2
    m[x][y] = 1
    for k in range(2, n * n + 1):
        if x == 0 and y == n - 1:
            x1, y1 = x + 1, y
        elif x == 0:
            x1, y1 = n - 1, y + 1
        elif y == n - 1:
            x1, y1 = x - 1, 0
        else:
            x1, y1 = x - 1, y + 1
        x, y = (x + 1, y) if m[x1][y1] else (x1, y1)
        m[x][y] = k
    return m

print(fun(3))
