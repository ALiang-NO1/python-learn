import requests
import os
import re
from bs4 import BeautifulSoup
from contextlib import closing
from tqdm import tqdm
import time

"""
description: 爬取动漫之家的动漫——《妖神记》
author: Jack Cui（2020）
modifier: ALiang（2021.3）
blog: https://blog.csdn.net/weixin_49012647
public-wechat: 【全面资源集】
"""

# 创建保存目录
save_dir = '妖神记'
if save_dir not in os.listdir('./'):
    os.mkdir(save_dir)

target_url = "https://www.dmzj.com/info/yaoshenji.html"

# 获取动漫章节链接和章节名
r = requests.get(url=target_url)
bs = BeautifulSoup(r.text, 'lxml')
list_con_li = bs.find('ul', class_="list_con_li")
cartoon_list = list_con_li.find_all('a')  # 获取章节链接标签（从后往前展示的），跳过ul、li标签直接查找a标签
chapter_names = []  # 章节名字列表
chapter_urls = []  # 章节链接
for cartoon in cartoon_list:
    href = cartoon.get('href')
    name = cartoon.text
    chapter_names.insert(0, name)  # 逆序插入，大章节在后面
    chapter_urls.insert(0, href)

# 下载漫画 
for i, url in enumerate(tqdm(chapter_urls)):
    download_header = {
        'Referer': url
    }
    name = chapter_names[i]
    # 去掉.
    while '.' in name:
        name = name.replace('.', '')
    chapter_save_dir = os.path.join(save_dir, name)
    if name not in os.listdir(save_dir):
        os.mkdir(chapter_save_dir)
    r = requests.get(url=url)
    html = BeautifulSoup(r.text, 'lxml')
    script_info = html.script   # 获取脚本标签
    pics = re.findall('\d{13,14}', str(script_info))  # 匹配到14位的数字，用列表储存
    for j, pic in enumerate(pics):  # 13位的最后面补0变成14位
        if len(pic) == 13:
            pics[j] = pic + '0'
    pics = sorted(pics, key=lambda x: int(x))  # 通过数字大小排序
    chapterpic_hou = re.findall('\|(\d{5})\|', str(script_info))[0]  # 匹配5位数字
    chapterpic_qian = re.findall('\|(\d{4})\|', str(script_info))[0]  # 匹配四位数字
    for idx, pic in enumerate(pics):
        if pic[-1] == '0':  # 也就是13位的数字
            url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic[:-1] + '.jpg'
        else:
            url = 'https://images.dmzj.com/img/chapterpic/' + chapterpic_qian + '/' + chapterpic_hou + '/' + pic + '.jpg'
        pic_name = '%03d.jpg' % (idx + 1)
        pic_save_path = os.path.join(chapter_save_dir, pic_name)
        with closing(requests.get(url, headers=download_header, stream=True)) as response:
            chunk_size = 1024  # 设置块大小
            content_size = int(response.headers['content-length'])
            if response.status_code == 200:
                with open(pic_save_path, "wb") as file:
                    for data in response.iter_content(chunk_size=chunk_size):
                        file.write(data)
            else:
                print('链接异常')
    time.sleep(10)
