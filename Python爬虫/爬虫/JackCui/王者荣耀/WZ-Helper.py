# -*- coding: UTF-8 -*-
import requests, json

import tkinter as tk
from tkinter import messagebox as msg

"""
文件说明：王者荣耀出装 GUI 程序
作者：ALiang
时间：2021-3-27
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
"""

# 通过 json 文件获取英雄 id
# file = json.load(open('英雄.json', 'r', encoding='utf8'))
# info = {}
# for i in file['list']:
#     info[i['name']] = int(i['hero_id'])
# print(info)

class WangZhe(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.headers = {'Accept-Charset': 'UTF-8',
                        'Accept-Encoding': 'gzip,deflate',
                        'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
                        'X-Requested-With': 'XMLHttpRequest',
                        'Content-type': 'application/x-www-form-urlencoded',
                        'Connection': 'Keep-Alive',
                        'Host': 'gamehelper.gm825.com'}
        self.ids = {'西施': 141, '甄姬': 21, '姜子牙': 37, '雅典娜': 60, '鬼谷子': 95, '鲁班七号': 8, '苏烈': 105, '亚瑟': 48, '镜': 143,
                    '曜': 139, '云中君': 136, '马超': 135, '盘古': 134, '嫦娥': 133, '猪八戒': 132, '瑶': 131, '上官婉儿': 129, '李信': 127,
                    '沈梦溪': 126, '伽罗': 125, '盾山': 124, '司马懿': 122, '孙策': 121, '元歌': 120, '米莱狄': 118, '狂铁': 117,
                    '裴擒虎': 116, '杨玉环': 115, '公孙离': 113, '弈星': 112, '明世隐': 110, '梦奇': 106, '百里玄策': 104, '女娲': 103,
                    '铠': 98, '百里守约': 96, '干将莫邪': 89, '黄忠': 66, '大乔': 65, '诸葛亮': 64, '东皇太一': 63, '太乙真人': 62, '蔡文姬': 61,
                    '哪吒': 59, '杨戬': 58, '成吉思汗': 57, '钟馗': 56, '虞姬': 55, '李元芳': 54, '张飞': 53, '刘备': 52, '后羿': 51,
                    '牛魔': 50, '孙悟空': 49, '橘右京': 47, '娜可露露': 46, '不知火舞': 45, '张良': 44, '艾琳': 43, '花木兰': 42, '兰陵王': 41,
                    '王昭君': 40, '韩信': 39, '刘邦': 38, '露娜': 36, '程咬金': 35, '安琪拉': 34, '貂蝉': 33, '关羽': 32, '老夫子': 31,
                    '武则天': 30, '项羽': 29, '达摩': 28, '狄仁杰': 27, '马可波罗': 26, '李白': 25, '宫本武藏': 24, '典韦': 23, '曹操': 22,
                    '夏侯惇': 20, '周瑜': 19, '吕布': 18, '芈月': 17, '白起': 16, '扁鹊': 15, '孙膑': 14, '钟无艳': 13, '阿轲': 12,
                    '高渐离': 11, '刘禅': 10, '庄周': 9, '孙尚香': 7, '嬴政': 6, '妲己': 5, '墨子': 4}
        self.master = master
        self.pack()
        self.createWidget()
        self.id = 25

    def get_id(self, name):
        if name in self.ids.keys():
            self.id = self.ids.get(name)
        else:
            msg.showerror('抱歉，没有该英雄！')

    def click_box(self, gear):
        self.id = int(gear.get(gear.curselection()).split('：')[-1])
        print(self.id)

    def createWidget(self):
        # 输入框：获取要查询的英雄
        name = tk.StringVar()
        name.set('李白')
        input = tk.Entry(self, textvariable=name)
        input.grid(row=0, column=0)
        tk.Button(self, text='查询', command=lambda: self.get_id(name.get()), takefocus=True).grid(row=0, column=1)
        # 列表盒子：列出可查询的英雄
        # frame = tk.Frame(self)
        box = tk.Listbox(self, width=50, height=10, background='lightblue')
        box.grid(row=1, column=0)
        for i in sorted(self.ids.items(), key=lambda x: x[1]):
            box.insert('end', f'{i[0]}: {i[1]}')
        box.bind('Double-Button-1', self.click_box)
        # 给盒子设置一个滚动条
        scroll_bar = tk.Scrollbar(self)
        scroll_bar.config(command=box.yview)
        scroll_bar.grid(row=1, column=0)

if __name__ == '__main__':
    root = tk.Tk()
    root.title('王者荣耀出装助手')
    root.geometry('500x600-10+10')
    app = WangZhe(master=root)
    root.mainloop()
