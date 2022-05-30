import os
from all import *

class Jiaoben:
    def __init__(self, tag, dir_name):
        self.dir_name = dir_name
        self.dict_list = []
        self.tag = tag
        self.dir_path = "E:\web素材\脚本素材\%s" % self.dir_name
        self.s = 1

    def get_hrefs(self, url):
        """获取页面总数及资源所在网址"""
        html = rq(url).text
        page_num = xp(html, '//div[@class="fenye"]/a/b/text()')[-1]     # 获取页面总数，返回所有标签元素，哎
        href_list = xp(html, '//div[@id="container"]/div/div/a/@href')      # 获取资源所在网页
        return page_num, href_list

    def get_dict(self, href):
        """获取资源名字及下载网址，以字典形式放入列表"""
        href = "https:" + href
        html = rq(href).content     # 搞了半天原来网页是字节流&#。。。
        name = xp(html, '//div[@class="text_wrap"]/h2/a/text()')[0] + '.rar'
        down_href = xp(html, '//div[@class="dian"]/a/@href')[-1]    # 列表中有12个下载网址，最后三个较好
        dic = {"name": name, "href": down_href}
        self.dict_list.append(dic)

    def save(self, dic):
        """保存资源，一个字典（文件）就调用一次"""
        # print(dic['href'])    # "http://downsc.chinaz.net/Files/DownLoad/templates/web3/chahua2641.rar"
        os.chdir(self.dir_path)
        if not os.path.exists(dic['name']):
            with open(dic['name'], 'wb') as f:
                f.write(rq(dic['href']).content)
                # print(f"{self.s}.{dic['name']} saved")
                self.s += 1

    def main(self):
        if not os.path.exists(self.dir_path):
            os.mkdir(self.dir_path)
            print(f"目录《{self.dir_name}》 创建成功！")
        url = "https://sc.chinaz.com/tag_jiaoben/%s.html" % self.tag
        n, l = self.get_hrefs(url)   # 总页数，资源所在网页
        if int(n) == 1:
            print("-------------正在爬取首页-------------")
            self.dict_list = []
            pool(self.get_dict, l, 35)
            print(self.dict_list)
            pool(self.save, self.dict_list, 35)
        else:
            page = 2
            while page <= int(n):
                self.dict_list = []
                pool(self.get_dict, l, 35)
                print(self.dict_list)
                # print(self.dict_list)
                pool(self.save, self.dict_list, 35)    # 先处理另外第一页，后面再覆盖变量
                print(f"-------------爬取到第{page}页-------------")
                url = "https://sc.chinaz.com/tag_jiaoben/%s_%s.html" % (self.tag, page)
                k, l = self.get_hrefs(url)
                page += 1

text = rq("https://sc.chinaz.com/tag_jiaoben/jianbianbeijing.html").content
tags = xp(text, '//p[@class="tags_a"]/a/@href')
# ['图片切换', '返回顶部', '动画效果', '倒计时', '弹出层', '在线客服', '手风琴', '表单代码', '文字特效', '滚动条', '瀑布流',
# '表单验证', '时钟代码', '抽奖转盘', '标签云', '播放器', '图片放大', '时间轴', '日历代码', '滚动代码', '选项卡', '进度条']
names = xp(text, '//p[@class="tags_a"]/a/text()')
i = 5
# while i < len(tags):
while i < 6:
    tag = tags[i].split('/')[-1].rstrip('.html')
    print(f"------------{names[i]}--------------")
    Jiaoben(tag, names[i]).main()
    i += 1