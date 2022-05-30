import os, time, requests, json, re, sys

import threadpool
from retrying import retry
from urllib import parse
from tqdm import tqdm

"""
文章描述：爬取王者荣耀英雄壁纸+封面
使用说明：直接在最底下输入下载地址，然后运行
作者：Felix(2020/7/30 14:42)
最新修改时间：2021-4-4
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
说明：（1）使用线程爬取，但是感觉没有快多少，网址图片加载速度不是很快，而且服务器会没有响应。
     （2）使用tqdm显示进度，但是该模块也会出问题，比如单位，img/s,结果变成s/img，而且加重程序负担
      (3)因为是二次更改，在函数里嵌套函数，非常不专业，所有尽量少用
"""

class HonorOfKings:
    """
     This is a main Class, the file contains all documents.
     One document contains paragraphs that have several sentences
     It loads the original file and converts the original file to new content
     Then the new content will be saved by this class
    """

    def __init__(self, save_path='./heros'):
        self.save_path = save_path  # 保存根目录默认在代码所在目录
        self.time = str(time.time()).split('.')
        self.url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=%s' % \
                   self.time[0]  # 抓包的网址

    def hello(self):
        """
        This is a welcome speech（欢迎界面）

        :return: self
        """
        print("*" * 50)
        print(' ' * 18 + '王者荣耀壁纸下载')
        print(' ' * 5 + '公众号：【全面资源集】')
        print("*" * 50)
        return self

    def pool(self, function, arg):
        """下载线程池"""
        pool = threadpool.ThreadPool(20)
        request = threadpool.makeRequests(function, arg)
        [pool.putRequest(req) for req in request]
        pool.wait()

    def run(self):
        """The program entry（程序入口）"""
        print('↓' * 20 + ' 格式选择: ' + '↓' * 20)
        print('1.缩略图 2.1024x768 3.1280x720 4.1280x1024 5.1440x900 6.1920x1080 7.1920x1200 8.1920x1440')
        size = input('请输入您想下载的格式序号，默认6：')
        print()
        size = size if size and int(size) in [1, 2, 3, 4, 5, 6, 7, 8] else 6

        hero_list = self.request(  # 下面网址是抓包获得的，暂时不会。。
            'http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8').json()
        cover_dicts = []  # 存放字典 {封面名：封面网址}
        hero_names = []  # 存放所有英雄名
        cover_div = os.path.join(self.save_path, '英雄封面')
        os.makedirs(cover_div)
        num = 0  # 下载第几张封面，用于显示进度
        all = len(hero_list['list'])
        def down_corver(dict):
            """下载封面"""
            global num
            content = self.request(dict['cover']).content
            cover_path = os.path.join(cover_div, dict['name'] + '.png')
            if not os.path.exists(cover_path):
                with open(cover_path, 'wb') as f:  # 保存封面
                    f.write(content)
                    num += 1
                    sys.stdout.write('\r')
                    sys.stdout.write('→ → → →正在爬取封面....爬取进度：%s|%s张' % (num, all))
        for i in hero_list['list']:
            cover_dicts.append({i['name']: i['corver']})
            hero_names.append(i['name'])
        # print(cover_dicts)
        for i in hero_names:
            os.makedirs(os.path.join(self.save_path, i))
        self.pool(down_corver, cover_dicts)

        page = 0
        offset = 0  # 爬取的页数
        total_res = self.request(self.url.format(page)).json()
        # total_response = self.request(self.url.format(page)).text
        # total_res = json.loads(total_response)
        total_page = --int(total_res['iTotalPages'])  # 所有页数
        print('→ → → →开始爬取皮肤（总共 {} 页）...'.format(total_page))

        def down(dict):
            """创建线程池下载"""
            if '-' in dict['name']:
                hero_name = dict['name'].split('-')[0]  # 英雄名，创建英雄图片目录
                hero_name = re.sub(r'[【】:.<>|·@#$%^&() ]', '', hero_name)
                for name in hero_names:
                    if name in hero_name:
                        hero_name = name
                save_path = os.path.join(self.save_path, hero_name)  # 英雄皮肤保存目录
                pic_name = dict['name'].split('-')[1]  # 各种皮肤名
                pic_name = re.sub(r'[【】:.<>|·@#$%^&() ]', '', pic_name) + '.jpg'
            else:
                hero_name = pic_name = dict['name']
                hero_name = pic_name = re.sub(r'[【】:.<>|·@#$%^&() ]', '', hero_name)
                save_path = os.path.join(self.save_path, hero_name)
            save_name = os.path.join(save_path, pic_name)
            hero_url = dict['url']
            if not os.path.exists(save_name):
                with open(save_name, 'wb') as f:
                    response_content = self.request(hero_url.replace("/200", "/0")).content
                    f.write(response_content)
            tq.update(1)
            time.sleep(0.4)

        while True:
            if offset > total_page:
                break
            url = self.url.format(offset)
            response = self.request(url).text
            result = json.loads(response)  # 共25页，每页20个图片，总共483张；每页英雄不同，即乱排的
            # now = 0
            dict_list = []  # 储存所有{英雄名：下载地址}的列表
            with tqdm(total=len(result["List"]), leave=False, unit='img', ncols=100) as tq:
                tq.set_description('第%s页' % offset)
                for item in result["List"]:
                    # now += 1
                    hero_name = parse.unquote(item['sProdName'])
                    # print('---正在下载第 {} 页 {} 英雄 进度{}/{}...'.format(offset, hero_name, now, len(result["List"])))
                    hero_url = parse.unquote(item['sProdImgNo_{}'.format(str(size))])
                    dict_list.append({'name': hero_name, 'url': hero_url})  # 把所有对应英雄名及图片下载地址放进列表
                self.pool(down, dict_list)
                offset += 1
        print('下载完成！')

    @retry(stop_max_attempt_number=3)
    def request(self, url):
        """
        Send a request

        :param url: the url of request
        :param timeout: the time of request
        :return: the result of request
        """
        response = requests.get(url, timeout=10)
        assert response.status_code == 200
        return response


if __name__ == "__main__":
    HonorOfKings(save_path=r'E:\win10\Pictures\电脑图片\王者荣耀壁纸').hello().run()