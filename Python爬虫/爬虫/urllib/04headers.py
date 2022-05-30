from urllib import request, parse

url = "https://mp.weixin.qq.com/s?src=3&timestamp=1610865113&ver=1&signature=NfJ1SMaZ831HZxZGHt571l8zf523M9oFA*Y61y9k-AUef6pgx4kQ4MytEuyCN4AvYBf-9UXvagKHY0GZuYsOgbKI5gun5YkKtDbUQUC6InEv2PCXWOwSGGFkhFS48wQBGW0TqATyA*jn6SNdPQEZW*LE4AltTx41I2syPruXl3E="
# 使用addheaders添加头
headers = ('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400')
opener = request.build_opener()
opener.addheaders = [headers]
print(opener.open(url).read().decode('utf-8'))

# 使用add_header添加头
# req = request.Request(url)
# req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
#                              'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400')
# print(request.urlopen(url, timeout=5).read().decode('utf-8'))