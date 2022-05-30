import requests
import pdfkit
from bs4 import BeautifulSoup
from sys import stdout

"""
文章描述：使用协程爬取菜鸟教程Python100例
作者：ALiang
最新修改时间：2021-4-19
公众号：【全面资源集】
博客：https://www.cnblogs.com/junmoye/
"""

# 渲染的html模板
html_template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <link type="text/css" rel="stylesheet" href="https://www.runoob.com/wp-content/themes/runoob/style.css?v=1.157">
    </head>
    <body>{}</body>
    </html>"""

def get_div():
    """获取所有例子的网页节点"""
    text = ''
    while True:
        try:
            i = yield text
            base_url = 'http://www.runoob.com/python/python-exercise-example' + str(i) + '.html'
            response = requests.get(base_url)
            soup = BeautifulSoup(response.content, 'html.parser')
            # 获取文档内容
            content = soup.find(class_='article-intro')
            # 删除第一个和最后一个 p 标签（Python 100例跳转链接）
            content.find_all('p')[0].decompose()
            content.find_all('p')[-1].decompose()
            # 去除图片
            while content.img:
                content.img.decompose()
            text += str(content)
        except Exception as e:
            print('wrong: %s' % e)
            continue

def save_pdf(func):
    """把所有html文件转换成pdf文件"""
    n = 0
    func.send(None)
    while n < 101:
        n += 1
        func.send(n)
        stdout.write('\r %s| %s/100' % (n // 2 * '▉', n))
    print('\n开始保存为PDF...')
    # options = {  # views视图中可以加上options进行页面布局调试　, options=options
    #     'page-size': 'Letter',
    #     'encoding': "UTF-8",
    #     'custom-header': [
    #         ('Accept-Encoding', 'gzip')
    #     ]
    # }
    path_wk = r"D:\program\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wk)
    pdfkit.from_string(html_template.format(func.send(n)), r'E:/PDF文档/python/python100例.pdf', configuration=config)

save_pdf(get_div())