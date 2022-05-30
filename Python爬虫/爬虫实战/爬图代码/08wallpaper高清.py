# 网站加载慢，容易爬到损坏的图
import requests
import os
import time
from lxml import etree
import threadpool

"""图片详情页：
https://wallhaven.cc/w/5dljv1   https://wallhaven.cc/w/n6g2l7
图片下载页：
https://w.wallhaven.cc/full/4l/wallhaven-4lo2dp.jpg     # /4l/*-4l...
https://w.wallhaven.cc/full/n6/wallhaven-n6dwr6.png
图片列表页：
https://wallhaven.cc/search?q=id%3A479&categories=110&purity=100&sorting=relevance&order=desc&page=5
图片缩略图网址：src="https://th.wallhaven.cc/small/z8/z8gr9y.jpg"   # 原图中可能是.png
"""

dit_list = []
dir_path = r"F:\img\wallpaper\toplist"    # 图片保存目录
url = "https://wallhaven.cc/toplist"

html = etree.HTML(requests.get(url).text)
href_list = html.xpath('//img[@alt="loading"]/@data-src')    # 图片所在网址
"""<img alt="loading" class="lazyload loaded" data-src="https://th.wallhaven.cc/small/z8/z8gr9y.jpg" src="https://th.wallhaven.cc/small/z8/z8gr9y.jpg">"""

def get_dit(href):
    """获取网址名及图片下载地址字典"""
    try:
        # html2 = etree.HTML(requests.get(href).text)   # 可能由于网页加载慢，得到的是429错误页，获取不到图片所在网址
        # src = html2.xpath('//img[@id="wallpaper"]/@src')[0]
        # name = src.split('/')[-1]
        name = href.split('/')[-1]
        src = "https://w.wallhaven.cc/full/" + name[:2] + '/wallhaven-' + name
        dit = {'name': name, 'src': src}
        dit_list.append(dit)
    except IndexError as e:
        print("src索引错误：", e, href)

s = 1
def spider(dit):
    """保存图片"""
    global s
    img_path = os.path.join(dir_path, dit['name'])
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
            res = requests.get(dit['src'], timeout=5)
            try:
                if res.status_code == 404:
                    f.write(requests.get(dit['src'].replace('.jpg', '.png'), timeout=5).content)
                else:
                    f.write(res.content)
                print(str(s) + '.' + dit['name'] + ":保存成功！")
            except ConnectionError as e:
                print("超时错误：", e)
    else:
        print(dit['name'], "已存在！")
    s += 1

def main(function, arg):
    pool = threadpool.ThreadPool(20)
    request = threadpool.makeRequests(function, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()

start = time.time()
main(get_dit, href_list)
print("get_dit()花费时间：", time.time()-start)
print(dit_list)
main(spider, dit_list)
print("spider()花费时间：", time.time()-start)