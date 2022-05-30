import re
import requests
import os

"""
文章描述：爬取美桌网（原美图网）所有分类图片
作者：ALiang
最新修改时间：2021-3-22
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
"""


bzzt_list = ['http://m.win4000.com/bzzt/index.html', 'http://m.win4000.com/bzzt/index2.html',
             'http://m.win4000.com/bzzt/index3.html', 'http://m.win4000.com/bzzt/index4.html',
             'http://m.win4000.com/bzzt/index5.html']   # 壁纸主分页网址
sjzt_list = ['http://m.win4000.com/sjzt/index.html', 'http://m.win4000.com/sjzt/index2.html',
             'http://m.win4000.com/sjzt/index3.html', 'http://m.win4000.com/sjzt/index4.html',
             'http://m.win4000.com/sjzt/index5.html']   # 手机壁纸主分页网址

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}

def rq(url):
    """请求资源"""
    response = requests.get(url, headers=headers)
    return response

def re_p1(str1):
    """匹配图片所在网址"""
    pattern1 = '<a href="(.*?)">.*?title="(.*?)".*?</a>'
    return re.findall(pattern1, str1)

def re_p2(str2):
    """匹配图片下载网址"""
    pattern2 = '<div class="xq_cont">.*?<img src="(.*?)">.*?</a>\s</div>'
    return re.findall(pattern2, str2, re.S)
"""<div class="xq_cont">
        <a href="http://m.win4000.com/wallpaper_detail_174372_2.html">
            <img src="http://pic1.win4000.com/wallpaper/2020-09-30/5f744d94d4e08.jpg">
        </a>
    </div>"""
def re_p3(str3):
    """匹配下一张图片链接网址"""
    pattern3 = '<div class="xq_cont">.*?<a href="(.*?)">.*?</a>.*?</div>'
    return re.findall(pattern3, str3, re.S)

def re_p4(str4):
    pattern = '<div class="ym">.*?<a href="(.*?)">下一页</a>'
    return re.findall(pattern, str4)

s = 1
bzzt_urls = []
for index_url in bzzt_list:  # 爬取手机壁纸是把bzzt_list换为sjbz_list
    while True:
        try:
            page_url = index_url    # 每页专题（index_url)有24种小分类
            # for page in range(5):
            list0 = re_p1(rq(page_url).text)  # 返回所有某大分类下的网址及类名元组列表[(url,‘二次元’)]
            for i in list0:
                if i[0].startswith('\\'):  # 分类网址无效，删除
                    list0.remove(i[0])
                dir_name = i[1]  # 大分类名
                print(dir_name)
                dir_path = os.path.join(r"F:\壁纸图片\电脑壁纸", dir_name)  # 大分类文件路径
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)

                response2 = rq(i[0]).text  # 请求大分类中某个小分类的网页代码
                list2 = re_p1(response2)  # 获取某小分类的具体图片页面网址（含图片所在网址及下一页网址）

                for j in list2:
                    if not j[0].startswith('/'):    # 过滤非网址
                        bzzt_urls.append(j[0])
                        img_name = j[1]  # 图片的名字

                        next_url = j[0]  # 下一页网址
                        for i in range(5):  # 5表示这类图片爬取5张，数量自定
                            response = rq(next_url).text  # 获取图片所在网页代码
                            src = re_p2(response)[0]  # 图片下载网址
                            content = rq(src).content  # 获取图片的二进制编码
                            # 图片保存路径
                            pic_path = os.path.join(dir_path, img_name + str(i + 1) + '.jpg')
                            # 保存图片
                            if not os.path.exists(pic_path):
                                with open(pic_path, 'wb') as f:
                                    f.write(content)
                                    print("%s.%s%s：保存成功！" % (s, img_name, str(i+1)))
                                    s += 1
                            else:
                                print(str(img_name) + str(i+1) + "已存在！")
                            next_url = re_p3(response)[0]
            # page_url = re_p4(rq(page_url).text)  # 获取下一页网址， 共5页
        except Exception as e:
            print("错误：", e)
            continue
with open("F:\壁纸\电脑壁纸\\bzzt_url.txt", 'w') as t:
    for x in bzzt_urls:
        t.write(x + '\n')
    print("urls文本文件保存成功！")