# -*- coding: UTF-8 -*-
import requests

import tkinter as tk

"""
文件说明：王者荣耀出装 GUI 程序
作者：ALiang
时间：2021-3-27
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
"""

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
        self.master = master
        self.pack()
        self.createWidget()

    def hero_weapon(self):  # 返回武器信息
        weapon_url = "http://gamehelper.gm825.com/wzry/equip/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
        req = requests.get(url=weapon_url, headers=self.headers).json()
        weapon_info_dict = req['list']
        return weapon_info_dict

    def seek_weapon(self, equip_id):  # 返回装备名字与价格
        for each_weapon in self.hero_weapon():
            if each_weapon['equip_id'] == str(equip_id):
                weapon_name = each_weapon['name']
                weapon_price = each_weapon['price']
                return weapon_name, weapon_price

    def hero_list(self):  # 获取所有英雄ID信息
        heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
        req = requests.get(url=heros_url, headers=self.headers).json()
        flag = 0
        id_info = ''
        for each_hero in req['list']:
            flag += 1
            id_info += '%s的ID为:%s' % (each_hero['name'], each_hero['hero_id']) + '||------------||'
            if flag == 4:
                id_info += '\n'
                flag = 0
        return id_info

    def get_hero_info(self, hero_id):  # 获取英雄信息字典
        hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8".format(
            hero_id)
        req = requests.get(url=hero_url, headers=self.headers).json()
        return req

    def createWidget(self):
        tk.Label(self, text='\n***欢迎使用王者荣耀出装助手***\n', foreground='#5a7bd3',
                 font='宋体 15 bold').pack()

        tk.Label(self, text='英雄ID表', font='黑体 16 bold', foreground='#800000').pack()
        tk.Label(self, text=self.hero_list(), width=105, height=16).pack()

        tk.Label(self, text='请输入要查询的英雄ID：', foreground='#800000').pack()
        id = tk.StringVar()
        self.id_input = tk.Entry(self, textvariable=id)
        self.id_input.pack()

        def show_info():
            num = self.id_input.get()
            hero_info = self.get_hero_info(num)
            print('id:', num)
            self.lable_history_hero['text'] = '历史上的%s' % hero_info['info']['name']
            self.lable_history_hero_intro['text'] = hero_info['info']['history_intro']
            battle_text = hero_info['info']['skill_tips'] + '\n\n' + hero_info['info']['recommend_summoner_skill_tips'] + '\n\n' + hero_info['info']['hero_tips'] + hero_info['info']['melee_tips']
            self.lable_battle_tip['text'] = battle_text
            self.lable_equipment['text'] = get_equipment_info(hero_info)

        tk.Button(self, text='确定', command=show_info).pack()

        self.lable_history_hero = tk.Label(self, text='', foreground='#800000')
        self.lable_history_hero.pack()
        self.lable_history_hero_intro = tk.Label(self, text='', width='105', height=6, bg='#a2eef0')
        self.lable_history_hero_intro.pack()

        tk.Label(self, text='英雄作战提示', foreground='#800000').pack()
        self.lable_battle_tip = tk.Label(self, text='', width=105, height=6, bg='#a2eef0')
        self.lable_battle_tip.pack()

        def get_equipment_info(hero_info):  # 获取出装信息
            text = ''
            for each_equip_choice in hero_info['info']['equip_choice']:
                text += '\n%s:\n   %s' % (each_equip_choice['title'], each_equip_choice['description'])
                total_price = 0
                flag = 0
                for each_weapon in each_equip_choice['list']:
                    flag += 1
                    weapon_name, weapon_price = self.seek_weapon(each_weapon['equip_id'])
                    text += '%s:%s' % (weapon_name, weapon_price) + ' ' * 4
                    total_price += int(weapon_price)
                text += '\n神装套件价格共计:%d' % total_price
            return text

        tk.Label(self, text='出装', foreground='#800000').pack()
        self.lable_equipment = tk.Label(self, text='', width=105, height=6, bg='#a2eef0')
        self.lable_equipment.pack()


if __name__ == '__main__':
    root = tk.Tk()
    root.title('王者荣耀出装助手')
    root.geometry()
    app = WangZhe(master=root)
    root.mainloop()
