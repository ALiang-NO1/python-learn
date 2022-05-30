html='''
<div class="panel">
    <div class="panel-heading">
        <h4>Hello</h4>
    </div>
    <div class="panel-body">
        <ul class="list" id="list-1">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
            <li class="element">Jay</li>
        </ul>
        <ul class="list-small" id="list-2">
            <li class="element">Foo</li>
            <li class="element">Bar</li>
        </ul>
    </div>
</div>
'''
from bs4 import BeautifulSoup
soup = BeautifulSoup(html, 'lxml')
print("第一个div标签中的所有内容：", soup.div)     # 获取第一个div标签中的所有内容
print("第一个div标签中的class值：", soup.div["class"])    # 获取第一个div标签的class的值
print("----------CSS选择器----------")
print("输出class的元素：", soup.select('.panel .panel-heading'))    # .代表class，中间需要空格来分隔
print(".panel-body .list-small:", soup.select(".panel-body .list-small")[0]['id'])     # [0].li
print("li标签：", soup.select('ul li'))   # 选择ul标签下面的li标签
print("list2下的element：", soup.select('#list-2 .element'))    # '#'代表id。这句的意思是查找id为"list-2"的标签下的，class=element的元素
print("节点类型：", type(soup.select('ul')[0]))   # 打印节点类型
print("----------层层嵌套选择----------")
for ul in soup.select('ul'):
    print(ul.select('li'))