from urllib import parse, request
from http import cookiejar

# "https://www.zhihu.com/people/liang-46-23"
data = bytes(parse.urlencode({'username': '', 'password': ''}), encoding='utf-8')
req = request.Request("https://www.zhihu.com/api/v3/oauth/sign_in", data)
cjar = cookiejar.CookieJar()
opener = request.build_opener(request.HTTPCookieProcessor(cjar))
request.install_opener(opener)
with open('zh.html', 'w') as f:
    file = opener.open(req).read()
    f.write(file)
    print("s")
