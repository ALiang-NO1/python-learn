import requests
from lxml import etree
import time
import random
import csv


def get_target(keyword, page):
    for i in range(1, page + 1):
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 '
                                 '(KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        url = 'https://search.bilibili.com/all?keyword={0}&from_source=nav_suggest_new0&page={1}'.format(keyword, page)
        html = requests.get(url.format(i), headers=headers)
        bs = etree.HTML(html.text)
        items = bs.xpath('//li[@class = "video-item matrix"]')
        for item in items:
            title = item.xpath('div[@class = "info"]/div/a/@title')[0]
            click = item.xpath('div[@class = "info"]/div[3]/span[1]/text()')[0].strip('\n        ').replace("万", "")
            danmu = item.xpath('div[@class = "info"]/div[3]/span[2]/text()')[0].strip('\n        ')
            date = item.xpath('div[@class = "info"]/div[3]/span[3]/text()')[0].strip('\n        ')
            up = item.xpath('div[@class = "info"]/div[3]/span[4]/a/text()')[0].strip('\n        ')
            data = {'标题': title, '播放量(万)': click, '弹幕': danmu, '日期': date, 'UP主': up}
            with open('B站数据.csv', 'a+', encoding='utf_8_sig', newline='') as fp:
                fieldnames = ['标题', '播放量（万）', '弹幕', '日期', 'UP主']
                writer = csv.DictWriter(fp, fieldnames=fieldnames)
                writer.writerow(data)
        time.sleep(random.random() + 1)
        print('已经完成b站第 {} 页爬取'.format(i))

if __name__ == "__main__":
    keyword = input("请输入要搜索的关键词：")
    page = int(input("请输入要爬取的页数："))
    get_target(keyword, page)