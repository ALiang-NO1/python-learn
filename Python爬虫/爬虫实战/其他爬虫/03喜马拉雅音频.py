import requests
import threadpool
from bs4 import BeautifulSoup
import re
import os
import random
import time

def getHtml(url):    # 获取网站 html 信息
    headers = {
        'User-Agent':
        'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'}
    # 用的代理 ip，如果被封的，在http://www.xicidaili.com/换一个
    proxy_addr = {'http': '221.7.255.168:8080'}
    html = requests.get(url, headers=headers, proxies=proxy_addr)   # 请求网页信息
    return html

def getId():    # 获取专辑的 id 和标题信息
    keyword = input('请输入你要查找的音频关键字:\n')     # 输入需要下载音频的关键字
    album_url = 'https://www.ximalaya.com/search/album/{}/sc/p1'.format(keyword)    # 输入关键字，拼接链接
    html = getHtml(album_url)
    soup = BeautifulSoup(html.text, 'lxml')
    info = soup.select('#searchPage div.search-type div.common-tab-content div.xm-loading ul div '
                       'a.xm-album-title.ellipsis-2')    # 提取音频文件的信息
    id_info = re.compile('href="/.*?"').findall(str(info))     # 提取专辑中 id
    title_info = re.compile('title=".*?"').findall(str(info))     # 提取专辑中标题信息
    ids = []
    titles = []
    for j in id_info:
        id = str(j).split('/')[2]
        ids.append(id)
    for t in title_info:
        # 处理下标题，防止创建文件夹失败
        title = str(t).split('"')[1].replace('\\', ' ').replace('/', ' ').replace(':', ' ').replace('*', ' ')\
            .replace('?', ' ').replace('"', ' ').replace('<', ' ').replace('>', ' ').replace('|', ' ')
        titles.append(title)
    return ids, titles, keyword

def down_4a(album_id):
    # 获取专辑下的音频总数
    count_url = 'https://www.ximalaya.com/revision/album/getTracksList?album_id={}&page_num=1'.format(album_id)
    count_html = getHtml(count_url)
    count_json = count_html.json()
    trackTotalCount = int(count_json['data']['trackTotalCount'])
    if trackTotalCount < 30 or trackTotalCount == 30:    # 音频数小于等于 30 时，只有一页
        page_num = 1
    else:
        if trackTotalCount % 30 == 0:                          # 音频数大于 30 时，且是30的倍数时
            page_num = trackTotalCount // 30
        else:
            page_num = (trackTotalCount // 30) + 1                  # 音频数大于 30 时，不是30的倍数时
    for num in range(1, page_num+1):
        m4a_url = 'https://www.ximalaya.com/revision/play/album?album_id={}&page_num={}&pageSize=30'.format(album_id, num)  # 拼接可下载音频信息的链接
        m4a_html = getHtml(m4a_url)
        m4a_json = m4a_html.json()
        for i in range(30):     # 一个页面最多30个音频文件
            try:
                trackName = m4a_json['data']['tracksAudioPlay'][i]['trackName']     # 提取音频标题
                src = m4a_json['data']['tracksAudioPlay'][i]['src']                 # 提取可下载链接
                # print(trackName)
                # print(src)
                if str(src) in ('null', 'None'):           # 如果为付费音频，则跳出循环，继续下载下一个专辑
                    print('此为付费音频，无法下载')
                    break
                data = requests.get(src).content
                with open('%s.m4a' % trackName, 'wb') as f:      # 下载音频
                    f.write(data)
            except IndexError:
                print('当前专辑已爬取完成！')
                continue

def mkdir():   # 判断目录是否存在，不存在的话则自动创建
    ids, titles, keyword = getId()
    for title, album_id in zip(titles, ids):
        print(title)
        path = 'E:\win10\Music\{}\{}'.format(keyword, title)   # 以音频名称命名
        isExists = os.path.exists(path)
        if not isExists:
            print('创建目录{}'.format(title))     # 目录不存在则创建一个
            os.makedirs(path)                     # 创建目录
            os.chdir(path)                        # 切换到创建的文件夹
            down_4a(album_id)                      # 调用函数下载音频到该目录下
        else:
            print('{}目录已存在,即将保存！'.format(title))
            os.chdir(path)                      # 切换到创建的文件夹
            down_4a(album_id)                    # 目录已存在时直接保存
        time.sleep(random.randint(2, 6))    # 随机等待

if __name__ == '__main__':
    mkdir()