from urllib.parse import *

"""
1.urlparse:将url分为6个部分，返回一个包含6个字符串项目的元组：协议、位置、路径、参数、查询、片段。
"""
url = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'
parse_url = urlparse(url)
print(parse_url)

"""
2.parse_qs: 获取urlparse分割后元祖中的某一项  urlparse(url).query   获取查询条件
实现方式：urlparse_qs 返回字典, urlparse_qsl 返回列表
"""
print('query:', parse_qs(parse_url.query))

"""
3.urlsplit: 和urlparse差不多，将url分为5部分，返回一个包含5个字符串项目的元组：协议、位置、路径、查询、片段。
"""
print(urlsplit(url))

"""
4.urljoin: 将相对的地址组合成一个url，对于输入没有限制，开头必须是http://，否则将不组合前面。
"""
print()
# 相当于 ./intro/overview.html，其中 . 指代当前文件夹 latest
print(urljoin('https://doc.scrapy.org/en/latest/index.html', 'intro/overview.html'))
# >>>"""https://doc.scrapy.org/en/latest  /intro/overview.html"""

# 当前网页某个tag id=walk-through-of-an-example-spider
print(urljoin('https://doc.scrapy.org/en/latest/intro/overview.html', '#walk-through-of-an-example-spider'))
# >>>https://doc.scrapy.org/en/latest/intro/overview.html  #walk-through-of-an-example-spider

# 相当于 ./install.html)
print(urljoin('https://doc.scrapy.org/en/latest/intro/overview.html', 'install.html'))
# >>>https://doc.scrapy.org/en/latest/intro  /install.html

# .. 指代当前文件夹intro的上一层文件夹latest)
print(urljoin('https://doc.scrapy.org/en/latest/intro/overview.html', '../topics/commands.html'))
# >>>https://doc.scrapy.org/en/latest  /topics/commands.html

