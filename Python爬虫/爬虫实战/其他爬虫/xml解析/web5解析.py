import xml.etree.ElementTree as etree

tree = etree.parse('web5.xml').getroot()
for url in tree.findall('url'):
    albumurl = url.find('albumurl').text
    webname = url.find('webname').text
    print(webname, albumurl)
