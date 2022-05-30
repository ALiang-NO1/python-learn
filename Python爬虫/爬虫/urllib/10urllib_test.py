from urllib.request import Request, ProxyHandler, build_opener, HTTPCookieProcessor, urlopen
from urllib.parse import quote
from http.cookiejar import CookieJar

url = 'http://cookdata.cn/#'

proxy = {'http': '58.22.177.214', 'https': '117.50.37.126:8111'}
handler = ProxyHandler(proxy)

cookie = CookieJar()
processor = HTTPCookieProcessor(cookie)

opener = build_opener(processor, handler)
res = opener.open(url)
print(res.status)
print(res.getheaders())
print(res.cookies)
for c in cookie:
    print('cookie:', c)

""" 证书认证
import ssl
context = ssl.create_default_context()
res = urlopen(res, context=context)
"""
