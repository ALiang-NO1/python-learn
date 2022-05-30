import requests
from PyPDF2 import PdfFileReader, PdfFileWriter
from bs4 import BeautifulSoup
import os
import shutil
import pdfkit

base_url = 'http://python3-cookbook.readthedocs.io/zh_CN/latest/'
book_name = ''
chapter_info = []
"""[
    {
        'title': 'first_level_chapter',     # 章节标题
        'url': 'www.xxxxxx.com',
        'child_chapters': [     # 章节下的小节
            {
                'title': 'second_level_chapter',
                'url': 'www.xxxxxx.com',
            }
            ...            
        ]
    }
    ...     # 许多个章节
]"""

def parse_title_and_url(html):
    """
    解析全部章节的标题和url

    :param html: 需要解析的网页内容
    :return None
    """
    soup = BeautifulSoup(html, 'html.parser')
    # 获取书名
    book_name = soup.find('div', class_='wy-side-nav-search').a.text
    menu = soup.find_all('div', class_='section')
    chapters = menu[0].div.ul.find_all('li', class_='toctree-l1')
    for chapter in chapters:
        # 获取一级标题和url，标题中含有'/'和'*'会保存失败
        info = {'title': chapter.a.text.replace('/', '').replace('*', ''), 'url': base_url + chapter.a.get('href'),
                'child_chapters': []}
        # 获取二级标题和url
        if chapter.ul is not None:
            child_chapters = chapter.ul.find_all('li')
            for child in child_chapters:
                url = child.a.get('href')
                # 如果在url中存在'#'，则此url为页面内链接，不会跳转到其他页面，所以不需要保存
                if '#' not in url:
                    info['child_chapters'].append({
                        'title': child.a.text.replace('/', '').replace('*', ''),
                        'url': base_url + child.a.get('href'),
                    })
        chapter_info.append(info)


html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
</head>
<body>
{content}
</body>
</html>
"""


def get_content(url):
    """
    解析URL，获取需要的html内容

    :param url: 目标网址
    :return: html
    """
    res = requests.get(url)
    res.encoding = 'utf-8'
    html = res.text
    soup = BeautifulSoup(html, 'html.parser')
    content = soup.find('div', attrs={'itemprop': 'articleBody'})
    html = html_template.format(content=content)
    return html


path_wk = r"D:\wkhtmltopdf\bin\wkhtmltopdf.exe"
config = pdfkit.configuration(wkhtmltopdf=path_wk)
def save_pdf(html, filename):
    """
    把所有html文件保存到pdf文件

    :param html:  html内容
    :param file_name: pdf文件名
    :return:
    """
    options = {
        'page-size': 'Letter',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'encoding': "UTF-8",
        'custom-header': [
            ('Accept-Encoding', 'gzip')
        ],
        'cookie': [
            ('cookie-name1', 'cookie-value1'),
            ('cookie-name2', 'cookie-value2'),
        ],
        'outline-depth': 10,
    }
    pdfkit.from_string(html, filename, options=options, configuration=config)


def parse_html_to_pdf():
    """
    解析URL，获取html，保存成pdf文件

    :return: None
    """
    try:
        for chapter in chapter_info:
            chapter_title = chapter['title']
            url = chapter['url']
            os.chdir(os.path.dirname(__file__))
            # 文件夹不存在则创建（多级目录）
            dir_name = os.path.join('gen', chapter_title)
            if not os.path.exists(dir_name):
                os.makedirs(dir_name)
            os.chdir(dir_name)

            html = get_content(url)
            save_pdf(html, chapter_title + '.pdf')

            children = chapter['child_chapters']
            if children:
                for child in children:
                    html = get_content(child['url'])
                    pdf_path = child['title'] + '.pdf'
                    save_pdf(html, pdf_path)
    except Exception as e:
        print('错误：', e)


def merge_pdf(infn_list, outfn):
    """
    合并pdf

    :param infn_list: 要合并的PDF文件路径列表，即 chapter_info
    :param outfn: 保存的PDF文件名
    :return: None
    """
    pagenum = 0
    pdf_output = PdfFileWriter()

    for pdf in infn_list:
        # 先合并一级目录的内容
        first_level_title = pdf['title']
        os.chdir(os.path.dirname(__file__))
        dir_name = os.path.join('gen', first_level_title)
        pdf_path = os.path.join(dir_name, first_level_title + '.pdf')

        pdf_input = PdfFileReader(open(pdf_path, 'rb'))
        # 获取 pdf 共用多少页
        page_count = pdf_input.getNumPages()
        for i in range(page_count):
            pdf_output.addPage(pdf_input.getPage(i))

        # 添加书签
        parent_bookmark = pdf_output.addBookmark(first_level_title, pagenum=pagenum)
        # 页数增加
        pagenum += page_count

        # 存子章节
        if pdf['child_chapters']:
            for child in pdf['child_chapters']:
                second_level_title = child['title']
                pdf_path = os.path.join(dir_name, second_level_title + '.pdf')

                pdf_input = PdfFileReader(open(pdf_path, 'rb'))
                # 获取 pdf 共用多少页
                page_count = pdf_input.getNumPages()
                for i in range(page_count):
                    pdf_output.addPage(pdf_input.getPage(i))

                # 添加书签
                pdf_output.addBookmark(second_level_title, pagenum=pagenum, parent=parent_bookmark)
                # 增加页数
                pagenum += page_count
    # 合并
    pdf_output.write(open(outfn, 'wb'))
    # 删除所有章节文件
    shutil.rmtree(os.path.dirname(__file__) + '/gen')

res = requests.get(base_url)
res.encoding = 'utf-8'
parse_title_and_url(res.text)
parse_html_to_pdf()
merge_pdf(chapter_info, r'E:\python3.pdf')