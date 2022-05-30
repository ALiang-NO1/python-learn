import requests

r = requests.get('https://www.douban.com/')
print(r.status_code)    # 输出状态码
print(r.encoding)   # 输出编码格式
print(r.headers)    # 输出头部文件
print(r.cookies)    # 输出cookie信息
print(r.content)    # 输出字节流形式网页源码
encodings = requests.utils.get_encodings_from_content(r.text)
print("-------encodings---------")
print(encodings)
encode_content = r.content.decode(r.encoding, 'replace').encode('utf-8', 'replace')  # 如果设置为replace，则会用?取代非法字符

# 爬取网页源码通用代码
def getHTMLText(url):
    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                                 'Chrome/79.0.3945.130 Safari/537.36'}  # 头部信息
        r = requests.get(url, headers=headers, timeout=30)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text   # 返回HTML代码
    except:
        return "产生异常"

"""请求头中的Content-Type字段已设置为application/x-www-form-urlencoded，
且d = {'key1': 'value1', 'key2': 'value2'}以form表单的形式提交到服务端，服务端返回的form字段即是提交的数据"""
url = 'https://www.baidu.com/'   # 这是公用网址
g = requests.get(url)
g.encoding = g.apparent_encoding
print(g.text)

# print("--------以form的形式发送请求----------")
# d = {'username': 'liang', 'pwd': '123456'}
# p = requests.get(url, data=d)

# print("--------以json的形式发送请求----------")
# s = json.dumps({'key1': 'value1', 'key2': 'value2'})
# p = requests.post(url, data=s)

# print("--------以multipart的形式发送请求----------")
# with open('report.txt', 'w') as f:
#     f.write('Hello Word!')
# files = {'file': open('report.txt', 'rb')}
# p = requests.post(url, files=files)