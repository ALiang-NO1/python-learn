a_set = {1, 3, 5}
a_set.add(8)
print('length: ', len(a_set))

a_set.update({2, 6})
print('用集合更新后：', a_set)

a_set.update([7, 9])
print('用列表更新后：', a_set)

a_set.discard(7)
print('删除10后：', a_set)

a_set.remove(9)
print('remove9后：', a_set)
print('9在集合中：', 9 in a_set)

print('删除并返回一个：', a_set.pop())

a_set.clear()
print('清空后：', a_set)

a_set.union({1, 2, 3, 8})
print('union(): ', a_set)
print('两个集合的交集：', a_set.intersection({1, 2, 3}))
print('两集合不相交的元素：', a_set.symmetric_difference({1, 2, 4, 6}))
print('是否为子集：', {1, 2}.issubset(a_set))
print('是否为父集：', a_set.issuperset({1, 2}))