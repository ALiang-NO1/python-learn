print('请输入三角形的三条边长!')
candidate = True
while candidate:
    a = int(input('请输入第一条边长:\n'))
    b = int(input('请输入第二条边长:\n'))
    c = int(input('请输入第三条边长:\n'))
    if a + b > c and a + c > b and b + c > a:
        if a == b == c:
            print('这是一个等边三角形。\n')
        elif a ** 2 + b ** 2 == c ** 2 or b ** 2 + c ** 2 == a ** 2 or a ** 2 + c ** 2 == b ** 2:
            print('这是一个直角三角形。')
        elif a ** 2 + b ** 2 > c ** 2 or a ** 2 + c ** 2 > b ** 2 or b ** 2 + c ** 2 > a ** 2:
            print('这是一个钝角三角形。\n')
        else:
            print('这是一个锐角三角形。\n')
    else:
        print('这不是三角形。\n')
    repeat = input("你想继续吗？（是/否）\n")
    if repeat == '否':
        candidate = False
