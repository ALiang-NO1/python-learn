import requests
import json
import openpyxl
import os

# 创建excel表格文档
fileName = "豆瓣.xlsx"
if not os.path.exists(fileName):
    file = openpyxl.Workbook()
    sheet0 = file.active
    sheet0.title = "douban"
    file.save(fileName)
    print("excel创建成功！")
# title_list = ['影名', '导演', '主演', '评分', '影片链接']
# sheet.append(title_list)

def spider(url, start):
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}
    param = {'sort': 'U',
             'range': '0,10',
             'tags': '',
             'start': start,
             'countries': '欧美'}
    response = requests.get(url, params=param, headers=headers).json()
    d = json.dumps(response)
    date = json.loads(d)
    print(date)
    # {'directors': ['克里斯·哥伦布'], 'rate': '9.1', 'cover_x': 4500, 'star': '45', 'title': '哈利·波特与魔法石', 'url': 'https:
    # //movie.douban.com/subject/1295038/', 'casts': ['丹尼尔·雷德克里夫', '艾玛·沃森', '鲁伯特·格林特', '艾伦·瑞克曼', '玛吉·史密斯']

    workbook = openpyxl.load_workbook('豆瓣.xlsx')
    sheet = workbook['douban']
    for i in date['data']:
        aa = ''
        bb = ''
        for a in i['directors']:
            aa += (a + '|')
        for b in i['casts']:
            bb += (b + '|')

        detail_dict = [i['title'], aa, bb, i['rate'], i['url']]
        sheet.append(detail_dict)
        workbook.save('豆瓣.xlsx')
    print("保存豆瓣信息成功！")
url = 'https://movie.douban.com/j/new_search_subjects'
spider(url, '20')
