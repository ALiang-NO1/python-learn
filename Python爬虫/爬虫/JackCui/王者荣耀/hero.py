# -*- coding: UTF-8 -*-
from urllib.request import urlretrieve
import requests
import os

"""
文件说明：获取并打印出王者荣耀出装信息
作者：Jack Cui
修改者：ALiang
时间：2021-3-21
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
"""

def hero_imgs_download(url, header):
    """
    下载《英雄联盟盒子》中的英雄图片

    :param url: GET请求地址，通过Fiddler抓包获取
    :param header: headers信息
    :return: none
    """
    req = requests.get(url=url, headers=header).json()
    hero_num = len(req['list'])
    print('一共有%d个英雄' % hero_num)
    hero_images_path = 'lol_images'  # 保存目录
    os.chdir(hero_images_path)
    for each_hero in req['list']:
        hero_photo_url = each_hero['cover']
        hero_name = each_hero['name'] + '.jpg'  # 图片名
        filename = os.path.join(hero_images_path, hero_name)
        if not os.path.exists(filename):  # 判断是否存在图片
            os.makedirs(hero_images_path)
        urlretrieve(url=hero_photo_url, filename=filename)


def hero_list(url, header):
    """
    打印所有英雄的名字和ID

    :param url: GET请求地址，通过Fiddler抓包获取
    :param header: headers信息
    :return: none
    """
    print('*' * 100)
    print('\t'*6, '欢迎使用《王者荣耀》出装助手！')
    print('*' * 100)
    req = requests.get(url=url, headers=header).json()
    flag = 0
    for each_hero in req['list']:
        flag += 1
        print('%s的ID为:%-7s' % (each_hero['name'], each_hero['hero_id']), end='\t\t')
        if flag == 4:
            print('\n', end='')
            flag = 0


def seek_weapon(equip_id, weapon_info):
    """
    根据equip_id查询武器名字和价格
    :param equip_id: 武器的ID
    :param weapon_info: 存储所有武器的字典
    :return: 武器的名字
    :return: 武器的价格
    """
    for each_weapon in weapon_info:
        if each_weapon['equip_id'] == str(equip_id):
            weapon_name = each_weapon['name']
            weapon_price = each_weapon['price']
            return weapon_name, weapon_price


def hero_info(url, header, weapon_info):
    """
    获取并打印出装信息
    :param url: GET请求地址，通过Fiddler抓包获取
    :param header: headers信息
    :param weapon_info: 存储所有武器的字典
    :return: none
    """
    req = requests.get(url=url, headers=header).json()
    print('\n历史上的%s：\n    %s' % (req['info']['name'], req['info']['history_intro']))
    print('性能提示：\n   ', req['info']['skill_tips'])
    print('推荐召唤师技能：\n', req['info']['recommend_summoner_skill_tips'])
    print('英雄提示：\n', req['info']['hero_tips'])
    print('操作技巧： \n', req['info']['melee_tips'])
    for each_equip_choice in req['info']['equip_choice']:
        print('\n%s:\n   %s' % (each_equip_choice['title'], each_equip_choice['description']))
        total_price = 0
        flag = 0
        for each_weapon in each_equip_choice['list']:
            flag += 1
            weapon_name, weapon_price = seek_weapon(each_weapon['equip_id'], weapon_info)
            print('%s:%s' % (weapon_name, weapon_price), end=' '*4)
            total_price += int(weapon_price)
        print('\n神装套件价格共计:%d' % total_price)


def hero_weapon(url, header):
    """
    获取武器信息
    :param url: GET请求地址，通过Fiddler抓包获取
    :param header: headers信息
    :return: 武器信息
    """
    req = requests.get(url=url, headers=header).json()
    weapon_info_dict = req['list']
    return weapon_info_dict


if __name__ == '__main__':
    headers = {'Accept-Charset': 'UTF-8',
               'Accept-Encoding': 'gzip,deflate',
               'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 6.0.1; MI 5 MIUI/V8.1.6.0.MAACNDI)',
               'X-Requested-With': 'XMLHttpRequest',
               'Content-type': 'application/x-www-form-urlencoded',
               'Connection': 'Keep-Alive',
               'Host': 'gamehelper.gm825.com'}
    # 所有装备信息网址
    weapon_url = "http://gamehelper.gm825.com/wzry/equip/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    # 所有英雄信息网址
    heros_url = "http://gamehelper.gm825.com/wzry/hero/list?channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8"
    hero_list(heros_url, headers)   # 列出所有英雄ID
    weapon_info_dict = hero_weapon(weapon_url, headers)  # 获取所有武器信息
    while True:
        hero_id = input("请输入要查询的英雄ID:")
        if not hero_id:
            break
        # 单个英雄信息网址（需要ID）
        hero_url = "http://gamehelper.gm825.com/wzry/hero/detail?hero_id={}&channel_id=90009a&app_id=h9044j&game_id=7622&game_name=%E7%8E%8B%E8%80%85%E8%8D%A3%E8%80%80&vcode=12.0.3&version_code=1203&cuid=2654CC14D2D3894DBF5808264AE2DAD7&ovr=6.0.1&device=Xiaomi_MI+5&net_type=1&client_id=1Yfyt44QSqu7PcVdDduBYQ%3D%3D&info_ms=fBzJ%2BCu4ZDAtl4CyHuZ%2FJQ%3D%3D&info_ma=XshbgIgi0V1HxXTqixI%2BKbgXtNtOP0%2Fn1WZtMWRWj5o%3D&mno=0&info_la=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&info_ci=9AChHTMC3uW%2BfY8%2BCFhcFw%3D%3D&mcc=0&clientversion=&bssid=VY%2BeiuZRJ%2FwaXmoLLVUrMODX1ZTf%2F2dzsWn2AOEM0I4%3D&os_level=23&os_id=dc451556fc0eeadb&resolution=1080_1920&dpi=480&client_ip=192.168.0.198&pdunid=a83d20d8".format(hero_id)
        hero_info(hero_url, headers, weapon_info_dict)  # 打印出装信息
