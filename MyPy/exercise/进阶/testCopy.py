import copy

# 测试深浅拷贝
a = [10, 10, [[10], 10, 10]]
b = copy.copy(a)

print("拷贝初始数据：")
print('a:', a)
print('b:', b)

# b.append((20))
# b[2].append(30)
# b[2][0].append(40)
# print("拷贝结果：")      # 列表第一层不变；内部层次为引用，改变
# print('a:', a)
# print('b:', b)

# 测试浅拷贝:shallow copy
c = copy.deepcopy(a)
c.append(20)
c[2].append(30)
c[2][0].append(40)
print("深拷贝结果：")
print('a:', a)
print('c:', c)