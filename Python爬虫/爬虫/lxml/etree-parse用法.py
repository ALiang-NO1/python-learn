from lxml import etree
from io import StringIO

test_html = '''
<html>
    <body>
        <div>div1
            <!-- 这里是注释 -->
            <h4>手机品牌商<span style="margin-left:10px">4</span></h4>
            <ul>
               <li>小米</li>
               <li>华为</li>
               <li class='blank'> OPPO </li>
               <li>苹果</li>
            </ul>`
        </div>
        <div>div2
            <h4>电脑品牌商<span style="margin-left:10px">3</span></h4>
            <ul class="ul" style="color:red">
                <li>戴尔</li>
                <li>机械革命</li>
                <li>ThinkPad</li>
            </ul>
        </div>
    </body>
</html>'''

html = etree.parse(StringIO(test_html))
print(html)
# 获取所有 li 标签数据
li_list = html.xpath('//li')

print("类型：", type(li_list))
print("值：", li_list)
print("个数：", len(li_list))

for l in li_list:
    print("li文本为：" + l.text)

print("---------属性操作---------")
ul = html.xpath('//ul')[1]

for name, value in ul.attrib.items():   # 遍历属性
    print('{0}="{1}"'.format(name, value))

ul.set("new_attr", "true")      # 添加新的属性
new_attr = ul.get('new_attr')   # 获取单个属性值
print('新属性的值：', new_attr)

# 获取最后一个div标签数据
last_div = html.xpath('//div[last()]')
print("last_div:", last_div)
print("最后一个div标签TAG：", last_div[0].tag, last_div[0].text)

# 添加子节点
child = etree.Element("child")
child.text = "这里是新的子元素"
last_div[0].append(child)
# 在最后一个 div 标签查找新的子元素
clild_text = last_div[0].find("child").text
print(clild_text)

print("---------删除元素--------")
# 查找并设置第一个查询到的元素
first_ul = html.find("//ul")
ul_li = first_ul.xpath("li")
for li in ul_li:
    # 删除元素
    first_ul.remove(li)

ul_li = first_ul.xpath("li")
if len(ul_li) == 0:
    print("元素被删除了")

# 遍历元素后代
body = html.find("body")
print(type(body))
for sub in body.iter():
    print("--sub.tag:", sub.tag)
    print("--sub.text:", sub.text)