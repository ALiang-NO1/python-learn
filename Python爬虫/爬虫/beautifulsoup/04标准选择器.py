html = '''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <p link="hello">hello<p>word</p></p>
    <s>strong</s>
    <b>The Dormouse's story</b>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
    <img data-foo="value"></img>
</div>
'''
from bs4 import BeautifulSoup
import re
soup = BeautifulSoup(html, 'lxml')
# find返回单个元素（直接返回结果），
print("----------获取第一个ul元素---------")
print(soup.find('ul'))
print("ul类型：", type(soup.find('ul')))
print("查找page的结果：", soup.find('page'))
print("----------获取所有ul元素----------")
print(soup.find_all('ul', limit=1))    # 查找所有ul标签下的内容, 并限制返回个数为1
print("ul类型", type(soup.find_all('ul')[0]))    # 查看其类型
print("----------获取ul下的所有li----------")
for ul in soup.find_all('ul'):
    print(ul.find_all('li'))
print("-------------查找多个标签---------------")
print(soup.find_all(['p', 's']))
print("----------通过正则match()匹配-----------")
for tag in soup.find_all(re.compile("^b")):
    print(tag.name)
print("---------传入true，返回标签------------")
for tag in soup.find_all(True):
    print(tag.name, end='\t')
print("\n--------------传入方法--------------")
def has_class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')
soup.find_all(has_class_no_id)
print("----------通过keyword参数搜索------------")
soup.find_all(link='hello')
print("-------------通过attrs搜索---------------")
print(soup.find_all(attrs={"data-foo": "value"}))
print("----------通过tag搜索字符串内容-----------")
print(soup.find_all(text="hello"))
print("----------用recursive禁止搜索子代-----------")
print(soup.find_all('p'))
print(soup.find_all('p', recursive=False))
