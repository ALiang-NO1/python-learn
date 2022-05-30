import http.cookiejar
import urllib.request
from urllib import parse, error

filename = "cookie.txt"     # 保存cookie为文本
# cookie:客户端用于记录用户身份，维持登录信息，保存类型有很多种:
cookie1 = http.cookiejar.MozillaCookieJar(filename)     # 类型1
cookie2 = http.cookiejar.LWPCookieJar(filename)     # 类型2

handler = urllib.request.HTTPCookieProcessor(cookie1)   # 设置处理器，传入cookieJar
opener = urllib.request.build_opener(handler)       # 创建opener

login_url = ""
headers = {}

info = {}   # 传入数据（字典类型）
post_data = parse.urlencode(info).encode()      # 将数据转为二进制

request = urllib.request.Request(login_url, data=post_data, headers=headers)
try:
    response = opener.open(request)
except error.URLError as e:
    print(e.reason)
# 保存cookie对象
cookie1.save(ignore_discard=True, ignore_expires=True)
for item in cookie1:
    print(item.name+": "+item.value)

get_url = ""    # 使用账号密码登入后的网址，真正的网址（抓包查看）
get_request = urllib.request.Request(get_url, headers=headers)
get_response = opener.open(get_request)

# 保存cookie后直接从文件导入cookie
cookie = http.cookiejar.LWPCookieJar(filename)
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
handler = urllib.request.HTTPCookieProcessor(cookie)
opener = urllib.request.build_opener(handler)
response = opener.open("http://www.baidu.com")
get_url2 = ""
get_request2 = urllib.request.Request(get_url)
get_response2 = opener.open(get_request)
print(get_response2.read().decode())