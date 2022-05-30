from urllib import request, parse

# request:GET
response = request.urlopen('https://www.baidu.com', timeout=30)
print("--------使用urlopen读取的结果-----------")
print(response.read().decode('utf-8'))
print("响应信息：", type(response), end='\t')
print(response.status)      # .getcode()
print(response.getheaders())    # .info()
print(response.getheader("头部的Server:", 'Server'))

# 增加header
url = 'http://httpbin.org/post'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
           'Chrome/57.0.2987.133 Safari/537.36', 'Host': 'httpbin.org'}
# request: POST
dict1 = {'name': 'Germey'}
data = bytes(parse.urlencode(dict1), encoding='utf8')
req = request.Request(url=url, data=data, headers=headers, method='POST')
response = request.urlopen(req)
print("--------post方法read读取网页的结果-----------")
print(response.read().decode('utf-8'))