i = 1
def move(n, fr, to):
    global i
    print('这是第%d步:把%d号盘子从%s移动到%s' % (i, n, fr, to))
    i += 1
def hanoi(n, a, b, c):
    if n == 1:
        move(1, a, c)
    else:
        hanoi(n-1, a, c, b)
        move(n, a, c)
        hanoi(n-1, b, a, c)
if __name__ == '__main__':
    n = int(input('输入A上面盘子的数量:'))
    print('移动开始')
    hanoi(n, 'A', 'B', 'C')