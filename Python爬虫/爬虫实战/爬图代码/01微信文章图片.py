from bs4 import BeautifulSoup
import requests
import os
import threadpool

"""
文章描述：面向过程并使用线程池爬取微信文章所有图片
作者：ALiang
最新修改时间：2021-3-21
公众号：全面资源集
博客：https://blog.csdn.net/weixin_49012647
"""

url = "https://mp.weixin.qq.com/s/vd1DxCPNxfmLfL6086aHuw"  # 要爬取的文章网址
dir_path = "E:\win10\Pictures\其他\丁香花"  # 这里修改图片保存的目录（绝对地址）
if not os.path.exists(dir_path):
    os.mkdir(dir_path)
else:
    print(dir_path, "已经存在！")

headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}
html = requests.get(url, headers=headers)
soup0 = BeautifulSoup(html.text, 'lxml')
imgList = soup0.find_all('img')     # 获取所有img元素
img_urls = []

for img in imgList:     # 对每个img元素处理
    soup = BeautifulSoup(str(img), 'lxml')     # 再次解析img元素
    if soup.img.has_attr('data-src'):
        img_url = soup.img['data-src']      # 获取图片网址
        img_urls.append(img_url)
i = 1
def spider(url):
    global i
    for z in range(1):
        try:
            response = requests.get(url, headers=headers)

            image_path = os.path.join(dir_path, str(i) + '.jpg')
            if not os.path.exists(image_path):
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                    print("%s.jpg" % i, "保存成功！")
                    i += 1
            else:
                print(str(i) + '.jpg已存在！')
                i += 1
        except Exception as e:
            print("错误：", e)
            continue

pool = threadpool.ThreadPool(20)  # 线程池的个数，也就是同时下载的图片张数
request = threadpool.makeRequests(spider, img_urls[:-2])
[pool.putRequest(req) for req in request]
pool.wait()
print("图片下载完了！")