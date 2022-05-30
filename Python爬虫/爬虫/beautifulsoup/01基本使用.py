html = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title" name="dromouse">class=title tag<b>The Dormouse's story</b></p>
<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1"><!-- Elsie --></a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>
<p class="story"><img src="http://blank"</p>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')    # 传入解析器：lxml
# print(soup.prettify())    # 格式化代码，自动补全
# print("第一个a标签中的内容：", soup.a)  # 获取第一个a标签中的所有内容
# print("title中的内容:", soup.title.string)    # 得到title标签里的内容
# print("title中的内容（方法二）:", soup.get_text())
# print("title的类型：", type(soup.title))     # 查看类型
# print("head元素的完整内容：", soup.head)
# print("title的名字：", soup.title.name)
# print("获取p的属性方法1：", soup.p.attrs['name'])     # 获取p标签中，name这个属性的值
# print("获取p的属性方法2：", soup.p['name'])   # 另一种写法，比较直接)
# print("嵌套选择；", soup.head.title.string)

soup.find('p', class_='title').clear()  # 删除标签的文本

# p_extract = soup.p.extract()  # 删除第一个 p 标签返回
# print(p_extract)

# soup.p.decompose()  # 将文档树的第一个 p 标签完全销毁
print(soup.prettify())