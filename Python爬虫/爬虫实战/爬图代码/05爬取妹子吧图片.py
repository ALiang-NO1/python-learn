# 网址已失效。。。
import re
import os
import requests

"""性感妹子有135x12个网页，有6个这样的分类"""

def rq(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}
    response = requests.get(url, headers=headers)
    return response

def re_1(html):
    """获取跳转至文章的网址"""
    p = '<h2 class="entry-title"><a href="(.*?)".*?>(.*?)</a></h2>'
    return re.findall(p, html)

def re_2(html):
    """获取图片下载网址"""
    p = '<p style="text-align: center;">.*?src="(.*?)"/></a>'
    return re.findall(p, html)

s = 1
n = 1
dir_names = ["性感妹子", "日本妹子", "台湾妹子", "清纯妹子", "妹子自拍", "街拍美女", ]
for i in range(1, 2):
    h = 1
    try:
        url = 'https://www.mziba.cn/category-%s.html' % i   # 六个分类网址

        dir_name = dir_names[i-1]
        dir_path = os.path.join(r"F:\壁纸图片\妹子吧", dir_name)
        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

        for j in range(6, 8):     # 共6x12篇文章（每页纸有12篇文章）
            a = re.findall(r'\d', url)[0]
            url2 = url.replace(a, a+'_'+str(j))    # 分类网址的一百多页中的一个页面
            tuples_list = re_1(rq(url2).text)      # 某页的所有文章网址及小分类名
            for x in tuples_list:
                page_url = x[0]   # 获取其中一页的一篇文章网址网址
                response = rq(page_url).text   # 获取其中一页的一篇文章网址网页代码

                if i == 5:      # 单独处理没有名字的文章
                    imgDir_name = "妹子自拍%s" % h
                elif i == 6:
                    imgDir_name = "街拍美女%s" % h
                else:
                    imgDir_name = x[1]  # 获取图片目录名

                # 妹子自拍
                imgDir_path = os.path.join(dir_path, imgDir_name)   # 每篇文章的图片保存的文件夹路径
                if not os.path.exists(imgDir_path):
                    os.mkdir(imgDir_path)
                else:
                    print(imgDir_name, "已存在！")
                h += 1

                srcs = re_2(response)
                while n < len(srcs):     # 保存文章下所有图片
                    img_path = os.path.join(imgDir_path, str(n) + '.jpg')
                    content = rq(srcs[n]).content
                    if not os.path.exists(img_path):
                        with open(img_path, 'wb') as f:
                            f.write(content)
                            print(str(s) + "." + dir_name + str(n), "：保存成功！")
                    else:
                        print(n, '.jpg已存在！')
                    n += 1
                    s += 1
                if n > 30:
                    print(imgDir_name)    # 还不知道怎么处理超过30张图片的文章！！！
                    # break   # 如果文章图片大于30张就进行下一张
                n = 1
    except Exception as e:
        print("错误：", e)
        continue