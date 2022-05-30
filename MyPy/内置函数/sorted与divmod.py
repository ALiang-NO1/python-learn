d = {3: 'd', 4: 'a', 2: 'c', 1: 'a', 5: 'b'}
s = sorted(d.items(), key=lambda x: x[0])  # key 传入匿名函数，表示以键为参考排序
s2 = sorted(d.items(), key=lambda x: x[1])  # 如果两个键值对的 key 相等，默认按原先顺序放
print("sorted() 排序结果：")
print(s)
print(s2)
print(".sort() 排序结果：")
l = list(d.items())
print('list:', l)
l.sort()
l.sort(reverse=True)
print(l)

# print("-----divmod-----")
# d = divmod(12, 5)
# print(d)