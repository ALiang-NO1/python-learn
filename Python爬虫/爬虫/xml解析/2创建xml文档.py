import xml.etree.ElementTree as etree

new_feed = etree.Element('{http://www.w3.org/2005/Atom}feed')   # 创建根元素（名字空间+本地名）
attrib = {'lang': 'en'}   # 标准的 ElementTree 格式，{namespace}localname。  {http://www.w3.org/XML/1998/namespace}lang
new_feed.attrib = attrib
print(etree.tostring(new_feed))     # 序列化结果
print('获取属性值：', new_feed.get('lang'))