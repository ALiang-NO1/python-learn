age = int(input('请输入你的年龄：'))
if age < 4:
    print('Your admission cost is $0!')
elif age < 18:
    print('Your admission cost is $5!')
elif age < 65:
    print('Your admission cost is $10!')
else:
    print('Your admission cost is $18!')
