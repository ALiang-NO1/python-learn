import requests
from threading import Thread
import re
import os.path
from queue import Queue

sjzt_list = ['http://m.win4000.com/sjzt/index.html', 'http://m.win4000.com/sjzt/index2.html',
             'http://m.win4000.com/sjzt/index3.html', 'http://m.win4000.com/sjzt/index4.html',
             'http://m.win4000.com/sjzt/index5.html']   # 手机壁纸主分页网址

def rq(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}
    response = requests.get(url, headers=headers)
    return response

def re_p1(str1):
    pattern1 = '<a href="(.*?)">.*?title="(.*?)".*?</a>'
    return re.findall(pattern1, str1)

def re_p2(str2):
    """匹配图片下载网址"""
    pattern2 = '<div class="xq_cont">.*?<img src="(.*?)">.*?</a>\s</div>'
    return re.findall(pattern2, str2, re.S)

def re_p3(str3):
    """匹配下一张图片链接网址"""
    pattern3 = '<div class="xq_cont">.*?<a href="(.*?)">.*?</a>.*?</div>'
    return re.findall(pattern3, str3, re.S)

queue = Queue()

def get_list0(index_url):
    response1 = rq(index_url).text
    list0 = re_p1(response1)  # 返回所有某大分类下的网址及类名元组列表[(url,‘二次元’)]
    return list0

def get_dirPath(index_url):
        list0 = get_list0(index_url)
        for i in list0:
            try:
                dir_name = i[1]     # 大分类名
                dir_path = os.path.join("E:\win10\Pictures\手机图片", dir_name)      # 大分类文件路径
                if not os.path.exists(dir_path):
                    os.mkdir(dir_path)
                return dir_path
            except:
                continue

def queue_put(index_url):
    list0 = get_list0(index_url)
    for i in list0:
        try:
            response2 = rq(i[0]).text  # 请求大分类中某个小分类的网页代码
            list2 = re_p1(response2)  # 获取某小分类的具体图片页面网址（含图片所在网址及下一页网址）
            for element in list2:
                if not element[0].startswith('/'):
                    queue.put(element[0])
        except Exception as e:
            # print("queue_put错误：", e)
            continue

def get_j():
    if not queue.empty():
        j = queue.get()
        queue.task_done()
        return j

def get_picName():
    j = get_j()
    img_name = j[1]  # 图片的名字
    return img_name

def get_imgUrl():
    """获取下一页网址"""
    j = get_j()
    response3 = rq(j[0]).text    # 获取图片所在网页代码
    img_url = re_p3(response3)[0]
    return img_url

def get_response4():
    """获取图片的二进制编码"""
    response3 = get_imgUrl().text
    response4 = rq(re_p2(response3)[0]).content
    return response4

def change_imgUrl():
    img_url = get_imgUrl()
    text = rq(img_url).text
    next_url = re_p3(text)      # 获取下一页图片所在网址
    return next_url

def save_pic(index_url):
    """保存图片"""
    s = 1
    dir_path = get_dirPath(index_url)
    pic_path = os.path.join(dir_path, get_picName() + '.jpg')
    if not os.path.exists(pic_path):
        with open(pic_path, 'wb') as f:
            f.write(get_response4())
            print("%s、%s：保存成功！" % (s, get_picName()))
            s += 1

def save_imgUrl():
    imgUrl = get_j()
    with open("E:\win10\pictures\手机图片\sjzt_url.txt", 'w') as t:
        t.write(imgUrl + '\t')

if __name__ == '__main__':
    print("进程开始！")
    for index_url in sjzt_list:
        for i in range(10):
            t1 = Thread(queue_put(index_url))
            t1.start()
            t1.join()
        for i in range(10):
            t2 = Thread(save_pic(index_url))
            t2.start()
            t2.join()
    save_imgUrl()
    print("进程结束！！")

    # def ch_img(list2):
    #     n = 1
    #     list2 = spider()
    #     for j in list2:
    #         response3 = rq(j[0]).text
    #         response5 = rq(re_p2(response3)).text    # 获取下一页图片所在网址
    #         url = re_p3(response5)