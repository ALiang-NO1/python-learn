plain_code = input("请输入明文：")
for p in plain_code:
    if ord('a') <= ord(p) <= ord('z'):  # 将字母向右移三位
        print(chr(ord("a") + (ord(p) - ord("a") + 3) % 26), end='')
    else:
        print(p, end='')