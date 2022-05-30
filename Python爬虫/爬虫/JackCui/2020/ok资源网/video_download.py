import os
import ffmpy3
import requests
from bs4 import BeautifulSoup
from multiprocessing.dummy import Pool as ThreadPool

"""
description: 通过视频连接匹配获取视频并下载视频——《越狱第一季》全集
author: Jack Cui（2020）
modifier: ALiang（2021.3.23）
blog: https://blog.csdn.net/weixin_49012647
public-wechat: 【全面资源集】
"""

search_keyword = '越狱第一季'
search_url = 'http://www.jisudhw.com/index.php'
serach_params = {  # Request URl: https://www.okzyw.net/index.php?m=vod-search
    'm': 'vod-search'
}
serach_headers = {  # Request Headers
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36',
    'Referer': 'http://www.jisudhw.com/',
    'Origin': 'http://www.jisudhw.com',
    'Host': 'www.jisudhw.com'
}
serach_datas = {  # Form Data
    'wd': search_keyword,
    'submit': 'search'
}

video_dir = ''

r = requests.post(url=search_url, params=serach_params, headers=serach_headers, data=serach_datas)
r.encoding = 'utf-8'
server = 'http://www.jisudhw.com'
search_html = BeautifulSoup(r.text, 'lxml')
search_spans = search_html.find_all('span', class_='xing_vb4')
serach_res = {}  # 储存下载视频的网址
for span in search_spans:
    url = server + span.a.get('href')  # 拼接后的视频页面地址
    name = span.a.string
    print(name)
    print(url)
    video_dir = name
    if name not in os.listdir('./'):
        os.mkdir(name)

    detail_url = url
    r = requests.get(url=detail_url)
    r.encoding = 'utf-8'
    detail_bf = BeautifulSoup(r.text, 'lxml')
    num = 1
    for each_url in detail_bf.find_all('input'):  # 视频所有集下载网址标签
        if 'm3u8' in each_url.get('value'):
            url = each_url.get('value')
            if url not in serach_res.keys():
                serach_res[url] = num
            print('第%03d集:' % num)
            print(url)
            num += 1


def downVideo(url):
    num = serach_res[url]
    name = os.path.join(video_dir, '第%03d集.mp4' % num)
    ffmpy3.FFmpeg(inputs={url: None}, outputs={name: None}).run()


# 开8个线程池
pool = ThreadPool(8)
results = pool.map(downVideo, serach_res.keys())
pool.close()
pool.join()
