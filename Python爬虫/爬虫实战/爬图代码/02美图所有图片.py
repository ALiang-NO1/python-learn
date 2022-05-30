from bs4 import BeautifulSoup
import requests
import os
import time

"""
http://m.win4000.com/wallpaper_detail_171856_1.html
文章描述：爬取美桌网（原美图网）所有图片
作者：ALiang
最新修改时间：2021-3-22
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
"""

i = 171856  # 表示种类，改变数字就改变种类了
count = 1   # 保存的图片总数，开始设为1
start = time.time()  # 开始时间
print("-------爬取开始...--------")
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko)'
                         ' Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}
while i < (i+10):  # 这里表示爬取10类壁纸
    j = 1  # 表示第一张图片
    while j < 10:  # 10表示每张图下载10张，这基本够了。当然，根据需要，只要不超过最大的就行
        url = "http://m.win4000.com/wallpaper_detail_%s_%s.html" % (i, j)
        html = requests.get(url, headers=headers)
        soup = BeautifulSoup(html.text, 'lxml')
        img_name = soup.h1.string + str(i) + '_' + str(j)
        img_path = os.path.join(r"E:\win10\Pictures\精美图片", img_name + ".jpg")  # 这里修改图片保存目录
        img_url = soup.img['src']
        response = requests.get(img_url, headers=headers)

        if not os.path.exists(img_path):
            with open(img_path, 'wb') as f:
                f.write(response.content)
                print(img_name, "保存成功！")
                j += 1
                count += 1
    i += 1
    print("-------开始新一组：wallpaper_detail_%s--------" % i)
time = time.time() - start
print("共保存%s张图片，用时%s" % (count, time))
