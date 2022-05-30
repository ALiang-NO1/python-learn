import os, time, requests, json, re, sys
from retrying import retry
from urllib import parse

"""
文章描述：爬取王者荣耀英雄壁纸+封面
使用说明：直接在最底下输入下载地址，然后运行
作者：Felix(2020/7/30 14:42)
最新修改时间：2021-4-5
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
说明：没有使用进程，面向对象加过程，使用控制台输出显示进度，没有反扒机制，不识别UA，此文章调试了两天才趋近完美
"""

class HonorOfKings:
    """王者荣耀皮肤下载"""
    def __init__(self, save_path='./heros'):
        self.save_path = save_path  # 默认路径为：./heros
        self.time = str(time.time()).split('.')
        self.url = 'https://apps.game.qq.com/cgi-bin/ams/module/ishow/V1.0/query/workList_inc.cgi?activityId=2735&sVerifyCode=ABCD&sDataType=JSON&iListNum=20&totalpage=0&page={}&iOrder=0&iSortNumClose=1&iAMSActivityId=51991&_everyRead=true&iTypeId=2&iFlowId=267733&iActId=2735&iModuleId=2735&_=%s' % \
                   self.time[0]  # 这是抓包获得的，暂时不会。。

    def hello(self):
        """这是排面"""
        print("*" * 50)
        print(' ' * 18 + '王者荣耀壁纸下载')
        print(' ' * 5 + '公众号：【全面资源集】')
        print("*" * 50)
        return self

    def run(self):
        """爬虫主程序"""
        print('↓' * 20 + ' 格式选择: ' + '↓' * 20)
        print('1.缩略图 2.1024x768 3.1280x720 4.1280x1024 5.1440x900 6.1920x1080 7.1920x1200 8.1920x1440')
        size = input('请输入您想下载的格式序号，默认6：')
        print()
        size = size if size and int(size) in [1, 2, 3, 4, 5, 6, 7, 8] else 6  # 直接回车就选6

        hero_list = self.request('http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8').json()
        hero_names = []  # 上面网址是抓包获得的，暂时不会。。
        cover_div = os.path.join(self.save_path, '英雄封面')
        os.makedirs(cover_div)
        num = 0  # 下载第几张封面，用于显示进度
        all = len(hero_list['list'])
        for i in hero_list['list']:
            hero_names.append(i['name'])  # 把英雄名放入列表
            content = self.request(i['cover']).content
            cover_path = os.path.join(cover_div, i['name']+'.png')
            if not os.path.exists(cover_path):
                with open(cover_path, 'wb') as f:  # 保存封面
                    f.write(content)
                    num += 1
                    sys.stdout.write('\r')
                    sys.stdout.write('→ → → →正在爬取封面....爬取进度：%s|%s张' % (num, all))
        # print(hero_names)

        page = 0  # 第零页，用于获取英雄总数，并保存第零页图片
        offset = 20  # 页数，用于递增爬取不同页
        total_response = self.request(self.url.format(page)).text
        total_res = json.loads(total_response)
        total_page = --int(total_res['iTotalPages'])  # 总页数（25）
        print('→ → → →开始爬取皮肤...（总共 {} 页）'.format(total_page))
        while True:
            if offset > total_page:
                break
            url = self.url.format(offset)
            result = self.request(url).json()  # 获取json格式数据（不标准），但是能索引，你也可以用下面的
            # response = self.request(url).text
            # result = json.loads(response)
            now = 0  # 表示第几张图，用于显示进度
            for item in result["List"]:
                now += 1
                split_name = parse.unquote(item['sProdName']).split('-')
                hero_name = split_name[0]  # 英雄名，但是不规范
                hero_name = re.sub(r'[【】:.<>|·@#$%^&() ]', '', hero_name)  # 把垃圾符号弄掉
                for f in hero_names:  # 有些英雄名是：张良·幽兰居士，但是我希望所有同英雄皮肤放在一个目录下，所有加上这一步
                    if f in hero_name:
                        hero_name = f
                # print('---正在下载第 {} 页 {} 英雄 进度{}/{}...'.format(offset, hero_name, now, len(result["List"])))
                hero_url = parse.unquote(item['sProdImgNo_{}'.format(str(size))])  # 网址都被编码了，恶心
                save_path = os.path.join(self.save_path, hero_name)  # 图片保存路径
                try:  # 不是每个名字都有“-”
                    pic_name = split_name[1]
                    pic_name = re.sub(r'[【】:.<>|·@#$%^&() ]', '', pic_name)+'.jpg'  # 图片名也给它标准化
                except IndexError:
                    pic_name = hero_name+'.jpg'
                save_name = os.path.join(save_path, pic_name)
                if not os.path.exists(save_path):
                    os.makedirs(save_path)
                if not os.path.exists(save_name):
                    with open(save_name, 'wb') as f:
                        response_content = self.request(hero_url.replace("/200", "/0")).content
                        f.write(response_content)
                        sys.stdout.write('\r')  # 让输出不断更新
                        sys.stdout.write('第%s页 %s|第%s张' % (offset, '▋'*2*now, now))
            offset += 1
        print('\n下载完成！')

    @retry(stop_max_attempt_number=3)
    def request(self, url):
        response = requests.get(url, timeout=10)
        assert response.status_code == 200
        return response


if __name__ == "__main__":
    HonorOfKings(r'E:\win10\Pictures\电脑图片\王者荣耀壁纸').hello().run()  # 这里设置图片下载根目录