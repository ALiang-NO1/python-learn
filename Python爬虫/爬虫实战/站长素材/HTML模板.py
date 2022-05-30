import os
from all import *

"""1.线程池：获取跳转链接、保存资源、多目录文件同时保存"""

def get_page(url):
    """获取页面总数"""
    html = rq(url).text
    page_num = xp(html, '//div[@class="fenye"]/a/b/text()')[-1]     # 获取页面总数，返回所有标签元素，哎
    return page_num

def get_hrefs(url):
    """获取资源所在网址"""
    html = rq(url).text
    href_list = xp(html, '//div[@id="container"]/div/div/a/@href')      # 获取资源所在网页
    return href_list

def get_dict(href):
    """获取资源名字及下载网址，以字典形式放入列表"""
    href = "https:" + href
    html = rq(href).content     # 搞了半天原来网页是字节流&#。。。
    name = xp(html, '//div[@class="text_wrap"]/h2/a/text()')[0] + '.rar'
    down_href = xp(html, '//div[@class="dian"]/a/@href')[-1]    # 列表中有12个下载网址，最后三个较好
    dic = {"name": name, "href": down_href}
    dict_list.append(dic)

def save(dic):
    """保存资源，一个字典（文件）就调用一次"""
    if not os.path.exists(dic['name']):
        with open(dic['name'], 'wb') as f:
            f.write(rq(dic['href']).content)

text = rq("https://sc.chinaz.com/moban/YiLiaoBaoJian.html").content
tags = xp(text, '//div[@class="moban_list"]/ul/li/a/@href')     # 获取大类标签
names = xp(text, '//div[@class="moban_list"]/ul/li/a/text()')       # 获取类名
i = 1
while i < len(tags):
    tag = tags[i].split('/')[-1].rstrip('.html')
    print(f"***********{names[i]}", end='')
    os.chdir("E:\web素材\HTML模板")
    if not os.path.exists(names[i]):
        os.mkdir(names[i])
        print(f"目录《{names[i]}》创建成功！")
    os.chdir(names[i])

    url = "https://sc.chinaz.com/moban/%s.html" % tag
    page_num = get_page(url)
    print(f"***********（共{page_num}页）")
    print(f"--------------保存到第一页--------------")

    j = 2
    # while j < int(page_num)+1 and j < 13:
    dict_list = []
    href_list = get_hrefs(url)  # 资源所在网页
    pool(get_dict, href_list, 24)
    print(dict_list)
    pool(save, dict_list, 24)  # 先处理另外第一页，后面再覆盖变量
    url = "https://sc.chinaz.com/moban/%s_%s.html" % (tag, j)
    print(f"--------------保存到第{j}页--------------")
        # j += 1
    i += 1