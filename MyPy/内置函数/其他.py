a = 'capital'
a = a.capitalize()      # 首字母大写
print(a.isupper())      # 是否全部大写
print(a.istitle())

print('-------next迭代-----------')
b = (x**2 for x in range(6))
print(b)
for i in range(6):
    print(next(b))