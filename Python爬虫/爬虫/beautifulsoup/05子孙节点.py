html = """
<html>
    <head>
        <title>The Dormouse's story</title>
    </head>
    <body>
        <p class="story">
            Once upon a time there were three little sisters; and their names were
            <a href="http://example.com/elsie" class="sister" id="link1">
                <span>Elsie</span>
            </a>
            <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> 
            and
            <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>
            and they lived at the bottom of a well.
        </p>
        <p class="story">...</p>
"""


from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')    # 传入解析器：lxml
print("----------p标签下的所有行（放于列表中）----------")
print(soup.p.contents)    # 获取指定标签的子节点，类型是list
print("----------获取子节点（p的子元素整体）----------")
for i, children in enumerate(soup.p.children):    # i接受索引，children接受内容(list生成器)
    print(i, children)
print("-------------用repr获取多个内容---------")
for children in soup.p.children:
    print(repr(children))
print("----------用stripped_strings去掉空行------------")
for s in soup.p.stripped_strings:
    print(repr(s))
print("----------获取孙节点----------")
for i, child in enumerate(soup.p.descendants):    # i接受索引，child接受内容
    print(i, child)
print("----------获取父节点----------")
print(soup.a.parent)    # 获取指定标签的父节点
print("----------获取祖先节点----------")
print(list(enumerate(soup.a.parents)))    # 获取指定标签的祖先节点