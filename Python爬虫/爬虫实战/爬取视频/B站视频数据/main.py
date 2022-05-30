import sys
import time
import random
import requests
import csv
from lxml import etree
from run import Ui_Form
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui, QtWidgets

class MyPyQt_Form(QWidget, Ui_Form):
    def __init__(self):
        super(MyPyQt_Form, self).__init__()
        self.setupUi(self)

    def pushButton_click(self):
        self.textEdit_2.setText("下载中......")
        self.keyword = self.lineEdit.text()  # 关键字
        self.page = int(self.lineEdit_2.text())  # 页数
        # result = pd.DataFrame()
        for i in range(1, self.page + 1):
            time.sleep(random.random() + 0.5)
            headers = {
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
            url = 'https://search.bilibili.com/all?keyword={0}&from_source=nav_suggest_new0&page={1}'.format(
                self.keyword, self.page)
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
                with open('{0}/{1}视频数据.csv'.format(self.download_path, self.keyword), 'a+', encoding='utf_8_sig',
                          newline='') as fp:
                    fieldnames = ['标题', '播放量(万)', '弹幕', '日期', 'UP主']
                    writer = csv.DictWriter(fp, fieldnames=fieldnames)
                    writer.writerow(data)
            self.textEdit_2.append("第{0}页下载完成".format(i))
            self.textEdit_2.append("保存路径:{}".format(self.download_path))
            self.textEdit_2.append("文件名称:{}".format('{0}共{1}个视频数据.csv'.format(self.keyword, self.page * 20)))

    def setBrowserPath(self):
        self.download_path = QFileDialog.getExistingDirectory(self)
        self.textEdit.setText(self.download_path)