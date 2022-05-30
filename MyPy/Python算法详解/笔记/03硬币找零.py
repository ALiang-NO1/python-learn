coins = [0.01, 0.02, 0.05, 0.1, 0.2, 0.5, 1.0]
coin_num0 = input('硬币数量（空格分开）：').split()  # 5 4 3 7 2 4 10
coin_num = []
s = 0
for i in range(7):
    coin_num.append(int(coin_num0[i]))
    s += coins[i] * coin_num[i]
change = float(input('要找的零钱：'))
if s < change:
    print('零钱不够！')
else:
    i = 6
    while i >= 0:
        if change >= coins[i]:
            n = change // coins[i]
            if n >= coin_num[i]:
                n = coin_num[i]
            change -= n * coins[i]
            print(f'用了{n}个{coins[i]}元硬币！')
        i -= 1
