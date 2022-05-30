import requests
from lxml import etree
import os
from tqdm import tqdm
from multiprocessing import Pool

def rq(url, data=None):
    res = requests.get(url)
    return res

def xp(html, xpath):
    tree = etree.HTML(html)
    list = tree.xpath(xpath)
    return list

dir = 'E:\win10\Pictures\电脑图片\yijngying'
start = 0
count = 40
url = 'https://tool.yijingying.com/imagetools/wallpaper'    # json: /api.php?cid=360new&start=30&count=30
if not os.path.exists(dir):
    os.mkdir(dir)

info_list = []      # 储存标题和下载链接的字典
# /pai.php?cid=360new&start=%s&count=%count' % (start, count)
html = rq(url, data={'start': start, 'count': count}).text
etree = etree.HTML(html)
img_list = xp(html, '//div[@id="walBox"]/div/img')
for img in img_list:
    info_list.append({'url': etree.xpath('./@data-realurl'), 'title': etree.xpath('./@alt')})

os.chdir(dir)
def down(info):
    global t
    if not os.path.exists(info['title']+'.jpg'):
        with open(info['title']+'.jpg') as f:
            f.write(rq(info['url']).content)
    t.update(1)

pool = Pool(20)
with tqdm(desc='下载进度（张）', total=count, ncols=100, unit='z', unit_scale=True) as t:
    pool.map(down, info_list)