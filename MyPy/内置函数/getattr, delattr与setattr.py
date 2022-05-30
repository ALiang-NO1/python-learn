class A:
    name = '全面资源集'
    age = 20

a = A()
print(getattr(a, 'name'))  # 获取属性 name
print(getattr(a, 'age'))

setattr(a, 'job', '没有')  # 获取属性 job
print(getattr(a, 'job'))

delattr(a, 'age')  # 删除属性 age
print(a.age)  # 报错