import requests
import os
from lxml import etree
import threadpool

"""
文章描述：爬取 simple desktop 网站图片
作者：ALiang
创作时间：2020
最新修改时间：2021-3-28
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
"""

# def xpath(url, xpath):
#     html = etree.HTML(requests.get(url).text)
#     return html.xpath(xpath)

def get_dit(href):
    """
    获取图片名字及下载地址

    :param href: 图片所在的网址
    :return: 图片名、图片下载地址
    """
    # http://static.simpledesktops.com/uploads/desktops/2019/06/15/CMYK_1.png.625x385_q100.png（href）
    html2 = etree.HTML(requests.get(home_url + href).text)
    src = '.'.join(html2.xpath('//div[@class="edge"]/div[@class="desktop"]/a/img/@src')[0].split('.')[:-2])
    name = href.split('/')[-2]
    # http://static.simpledesktops.com/uploads/desktops/2019/06/15/CMYK_1.png（原图）
    dit = {'name': name, 'src': src}
    dit_list.append(dit)

def spider(dit):
    """
    保存图片

    :param dit: {图片名：图片下载地址}
    :return: none
    """
    global s
    img_path = os.path.join(r"F:\img\simpleDesk", dit['name'] + '.png')  # 图片保存路径（目录+图片名）
    if not os.path.exists(img_path):
        with open(img_path, 'wb') as f:
            f.write(requests.get(dit['src']).content)
            print(str(s) + '.' + dit['name'] + "保存成功！")
    else:
        print(dit['name'], "已存在！")
    s += 1

def my_pool(function, arg):
    """
    使用线程池下载图片

    :param function: 处理的函数/方法
    :param arg: 传给函数/方法的参数（这里是字典列表）
    :return: none
    """
    pool = threadpool.ThreadPool(50)
    request = threadpool.makeRequests(function, arg)
    [pool.putRequest(req) for req in request]
    pool.wait()

for page in range(1, 2):   # 每页有28张图
    print("--------------当前正在下载第%s页-------------" % page)
    s = 1  # 用于计数
    dit_list = []  # 储存图片名及图片下载地址组成的字典
    url = "http://simpledesktops.com/browse/%s/" % page  # 最先爬取的网址
    home_url = "http://simpledesktops.com"  # 用于拼接网址
    html = etree.HTML(requests.get(url).text)
    href_list = html.xpath('//div[@class="desktop"]/a/@href')
    # print(href_list)
    my_pool(get_dit, href_list)  # 先调用线程池保存字典
    my_pool(spider, dit_list)  # 调用线程池保存图片

    # from multiprocessing.dummy import Pool
    # pool = Pool(28)
    # pool.map(get_dit, href_list)
    # pool.map(spider, dit_list)