import os
from all import *

JieTouLiuXing = "https://sc.chinaz.com/yinxiao/JieTouLiuXing.html"

def get_dicts(url):
    """通过音效列表页获取下载网址及音效名"""
    text = rq(url).text
    all_div = xp(text, '//div[@class="text_left"]/div[@class="music_block"]')
    for div in all_div:
        href = 'https:' + div.xpath('./p[@class="n1"]/@thumb')
        name = div.xpath('./p[@class="z"]/a/text()') + '.mp3'
        dic = {"name": name, "href": href}
        dict_list.append(dic)

def save(dic):
    """保存资源，一个字典（文件）就调用一次"""
    if not os.path.exists(dic['name']):
        with open(dic['name'], 'wb') as f:
            f.write(rq(dic['href']).content)
            # print(f"{s}.{dic['name']} saved")
            # s += 1

home_dir = "F:\站长素材\音效"
url = "https://sc.chinaz.com/yinxiao/JieTouLiuXing.html"
res = rq(url).text
names = xp(res, '//div[@class="yxfenlei"]/ul/li/a/text()')
hrefs = xp(res, '//div[@class="yxfenlei"]/ul/li/a/@href')   # 用于获取tag
i = 0
dicts = []
while i < len(names):
    dic = {"name": names[i], "href": hrefs[i]}
    i += 1

os.chdir(home_dir)
def main(dic):
    """通过大类的名及网址获取目录名及标签"""
    tag = dic['href'].split('/')[-1].strip('.html')
    if not os.path.exists(dic['name']):
        os.mkdir(dic['name'])
        print(f"目录：{dic['name']} 创建成功！")
    os.chdir(os.path.join(home_dir, dic['name']))
    url = "https://sc.chinaz.com/yinxiao/%s.html" % tag
    page_num = xp(rq(url).text, '//div[@class="fenye"]/a/b/text()')[-1]  # 获取页面总数
    page = 2
    while page <= int(page_num):
        print(f"-------{dic['name']}:爬取到第{page}页------")
        url = "https://sc.chinaz.com/yinxiao/%s_%s.html" % (tag, page)
        dict_list = []
        get_dicts(url)
        print(dict_list)
        pool(save, dict_list, 40)    # 先处理另外第一页，后面再覆盖变量
        page += 1

pool(main, dicts, 20)