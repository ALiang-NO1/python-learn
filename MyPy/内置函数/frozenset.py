print(frozenset(range(10)))

a = frozenset('avavavav')
print('a:', a)

a2 = a.union({'b', 'c'})  # 将集合随意插入
print('a2:', a2)
print('issuperset?', a2.issuperset(a))

a3 = a.copy()
print(a3)

print('a2-a3', a3.difference(a))

# 'copy', 'difference', 'intersection', 'isdisjoint', 'issubset', 'issuperset', 'symmetric_difference', 'union']