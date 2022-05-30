from urllib import request, error

print("---------访问不存在的页面------------")
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.URLError as e:
    print('URLError:', e.reason)

print("---------先捕获子类错误------------")
try:
    response = request.urlopen('http://cuiqingcai.com/index.htm')
except error.HTTPError as e:
    print('HTTPError!', 'reason:', e.reason, "状态码：", e.code, "e的头部：", e.headers, sep='\n')
except error.URLError as e:
    print('URLError:', e.reason)
else:
    print('Request Successfully')

print("---------判断原因------------")
import socket
import urllib.error
try:
    response = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
except urllib.error.URLError as e:
    if isinstance(e.reason, socket.timeout):
        print('TIME OUT')

# 证书验证
import ssl
from urllib import request

url = ""
context = ssl.create_default_context()
res = request.urlopen(url, context=context)