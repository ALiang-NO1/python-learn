import requests
from tqdm import tqdm
from bs4 import BeautifulSoup

"""
description: 爬取新笔趣阁小说——《诡秘之主》保存为文本文档
author: Jack Cui（2020）
modifier: ALiang（2021.3）
blog: https://blog.csdn.net/weixin_49012647
public-wechat: 【全面资源集】
"""

def get_content(target):
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    bf = BeautifulSoup(html, 'lxml')
    texts = bf.find('div', id='content')
    content = texts.text.strip().split('\xa0' * 4)  # 通过\xa0分割段落
    return content


if __name__ == '__main__':
    server = 'https://www.xsbiquge.com'
    book_name = '诡秘之主.txt'
    target = 'https://www.xsbiquge.com/15_15338/'
    req = requests.get(url=target)
    req.encoding = 'utf-8'
    html = req.text
    chapter_bs = BeautifulSoup(html, 'lxml')
    chapters = chapter_bs.find('div', id='list')
    chapters = chapters.find_all('a')  # 获得所有章节标签
    for chapter in tqdm(chapters):  # 创建进度条显示爬取进度
        chapter_name = chapter.string
        url = server + chapter.get('href')
        content = get_content(url)
        with open(book_name, 'a', encoding='utf-8') as f:
            f.write(chapter_name)
            f.write('\n')
            f.write('\n'.join(content))
            f.write('\n')
