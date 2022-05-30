# -*- coding:UTF-8 -*-
import requests, re, json, sys
from bs4 import BeautifulSoup
from urllib import request

"""
description: 文章描述：通过解析网站下载视频
author: Jack Cui（2020）
modifier: ALiang（2021.4。12）
csdn: https://blog.csdn.net/weixin_49012647
public-wechat: 【全面资源集】
"""

class video_downloader():
    def __init__(self, url):
        self.server = 'http://api.xfsub.com'
        self.api = 'http://api.xfsub.com/xfsub_api/?url='
        self.get_url_api = 'http://api.xfsub.com/xfsub_api/url.php'
        self.url = url.split('#')[0]
        self.headers = {'Referer': 'http://api.xfsub.com/xfsub_api/?url=%s?qqdrsign=055a4' % self.url}
        self.target = self.api + self.url
        self.s = requests.session()

    def get_key(self):
        """获取key、time、url等参数"""
        req = self.s.get(url=self.target)
        req.encoding = 'utf-8'
        self.info = json.loads(re.findall('"url.php",\ (.+),', req.text)[0])  # 使用正则表达式匹配结果，将匹配的结果存入info变量中

    def get_url(self):
        """获取视频地址"""
        data = {'time': self.info['time'],
                'key': self.info['key'],
                'url': self.info['url'],
                'type': ''}
        req = self.s.post(url=self.get_url_api, data=data, headers=self.headers)
        url = self.server + json.loads(req.text)['url']
        req = self.s.get(url=url, headers=self.headers)
        bf = BeautifulSoup(req.text, 'xml')  # 因为文件是xml格式的，所以要进行xml解析。
        video_url = bf.find('file').string  # 匹配到视频地址
        return video_url

    def progress(self, a, b, c):
        """回调函数，打印下载进度"""
        per = 100.0 * a * b / c
        if per > 100:
            per = 1
        sys.stdout.write("  " + "%.2f%% 已经下载的大小:%ld 文件大小:%ld" % (per, a * b, c) + '\r')
        sys.stdout.flush()

    def video_download(self, url, filename):
        """视频下载"""
        request.urlretrieve(url=url, filename=filename, reporthook=self.progress)


if __name__ == '__main__':
    url = 'http://www.iqiyi.com/v_19rr7qhfg0.html#vfrm=19-9-0-1'
    vd = video_downloader(url)
    filename = '加勒比海盗5'
    print('正在下载：', filename)
    vd.get_key()  # 获取key time url
    video_url = vd.get_url()  # 获取视频地址
    print('获取地址成功：', video_url)
    vd.video_download(video_url, filename + '.mp4')
    print('\n下载完成！')
