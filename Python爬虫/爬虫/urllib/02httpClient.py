# -------------httpClient----------
from http.client import HTTPConnection
from urllib.request import urlopen

HTTPConnection.debuglevel = 1
print(urlopen('http://diveintopython3.org/examples/feed.xml').headers.as_string())


# -----------debuglog------------
from urllib import request

httphd = request.HTTPHandler(debuglevel=1)
httpshd = request.HTTPHandler(debuglevel=1)
opener = request.build_opener(httphd, httpshd)
request.install_opener(opener)
print(request.urlopen('https://www.baidu.com'))