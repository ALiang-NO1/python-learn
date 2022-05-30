html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1" name="elements">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print("根据属性字典标志查找并返回内容")
print(soup.find_all(attrs={'id': 'list-1'}))    # 传入的是一个字典类型，也就是想要查找的属性
print(soup.find_all(attrs={'name': 'elements'}))
print("-----------方法2：直接根据属性标志返回---------")
print(soup.find_all(id='list-1'))    # id是个特殊的属性，可以直接使用
print(soup.find_all(class_='element'))     # class是关键字所以要用class_
print("-----------查找Foo---------")
print(soup.find_all(text='Foo'))    # 查找文本为Foo的内容，但是返回的不是标签