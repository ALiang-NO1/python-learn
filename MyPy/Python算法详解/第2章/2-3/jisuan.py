price = {
    '小米': 899,
    '华为': 1999,
    '三星': 3999,
    '谷歌': 4999,
    '酷派': 599,
    'iPhone': 5000,
}

min_price = min(zip(price.values(), price.keys()))
print(min_price)

max_price = max(zip(price.values(), price.keys()))
print(max_price)

price_sorted = sorted(zip(price.values(), price.keys()))
print(price_sorted)

price_and_names = zip(price.values(), price.keys())
print((min(price_and_names)))

# print (max(price_and_names))  error  zip()创建了迭代器，内容只能被消费一次
print(min(price))
print(max(price))
print(min(price.values()))
print(max(price.values()))
print(min(price, key=lambda k: price[k]))
print(max(price, key=lambda k: price[k]))