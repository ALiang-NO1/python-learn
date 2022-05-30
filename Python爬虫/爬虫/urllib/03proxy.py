from urllib.request import ProxyHandler, build_opener

proxy = '175.44.109.53'   # 使用本地代理
# proxy = 'username:password@123.58.10.36:8080'   # 购买代理
proxy_handler = ProxyHandler({
    'http': 'http://'+proxy,
    'https': 'https://'+proxy
})
opener = build_opener(proxy_handler)
response = opener.open('http://www.baidu.com')  # 测试ip的网址
print(response.read().decode('utf-8'))

# ------------添加全局proxy配置---------
from urllib import request

proxy = request.ProxyHandler({'http': '113.121.37.163'})
opener = request.build_opener(proxy, request.HTTPHandler)
request.install_opener(opener)
print(request.urlopen("").read().decode('utf-8'))