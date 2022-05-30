n = input('请输入一个整数（在任意时刻输入“停止”来终止程序）：')
while True:
    if n == '停止':
        break
    else:
        if int(n) % 2 == 0:
            print('这是一个偶数。')
            n = input('请继续输入：')
            if n == '停止':
                break
        else:
            print('这是一个奇数。')
            n = input('请继续输入：')
            if n == '停止':
                break
