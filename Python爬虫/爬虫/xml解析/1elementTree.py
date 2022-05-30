import xml.etree.ElementTree as etree

tree = etree.parse('movies.xml')
root = tree.getroot()
print('根元素标签：', root.tag)
print('根的子元素个数：', len(root))
print('第二个子节点：', root[1], '；属性：', root[1].attrib)  # 返回属性字典

print('find方法：', root.find('movie').get('title'))  # 获取标签的属性值
print('findall方法：', root.findall('movie'))  # 返回类型列表

print('第一个type标签的文本：', root.find('movie').find('type').text)