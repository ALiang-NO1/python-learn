import requests
import os
import re
import time

i = 3
dir_name = "E:\win10\Pictures\图趣网每日一图"  # 设置图片保存地址
if not os.path.exists(dir_name):
    os.mkdir(dir_name)  # 创建目录
else:
    print("文件已存在：", dir_name)
while i <= 14:
    html = "http://www.tuquu.com/pic/index_%s.html" % i
    response = requests.get(html)
    response.encoding = response.apparent_encoding      # 设置编码格式，防乱码
    text = response.text    # 主网页的html代码
    # print(text)
    htmls = re.findall(r'<a href="(.*?)" title="(.*?)" target="(.*?)">', text)      # 匹配含有高清图的网址
    try:
        print("这是第%s页！" % i)
        i += 1
        count = 0
        # print(htmls)
        for h in htmls:
            img_path = dir_name + '\\' + h[1] + '.jpg'  # 设置图片路径
            if not os.path.exists(img_path):
                response1 = requests.get(h[0])
                response1.encoding = response1.apparent_encoding
                img_html = re.findall(r'<a href="(.*?)" rel=.*? class=.*?>.*?</a>', response1.text)     # 图片下载地址
                # print("匹配的所有内容：", img_html)
                response2 = requests.get(img_html[0])   # 请求地址
                # print(img_html[0])
                with open(img_path, 'wb') as f:
                    f.write(response2.content)
                    count += 1
                    print("第%s张:" % count, h[1], "保存成功。")
                    time.sleep(0.2)
    except Exception as e:
        print("爬取失败！错误如下：")
        print(e)