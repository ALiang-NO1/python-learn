import requests
import os
# from sys import stdout
from threadpool import makeRequests, ThreadPool
from tqdm import tqdm

"""
文章描述：
作者：ALiang
最新修改时间：2021-4-8
公众号：【全面资源集】
博客：https://blog.csdn.net/weixin_49012647
"""


dir = r'E:\园林树木学'
os.chdir(dir)
hrefs = ['http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12546', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12545', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12544', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12543', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12542', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12541', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12540', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12539', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12538', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12537', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12536', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12535', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12534', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12532', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12533', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12530', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12531', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12529', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12527', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12528', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12526', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12525', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12524', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12523', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12522', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12521', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12520', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12519', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12518', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12517', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12516', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12515', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12514', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12513', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12512', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12511', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12510', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12509', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12508', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12507', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12506', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12505', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12504', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12503', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12502', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12500', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12501', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12499', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12498', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12497', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12496', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12495', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12494', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12493', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12492', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12491', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12490', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12489', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12488', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12486', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12487', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12485', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12484', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12483', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12482', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12481', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12480', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12479', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12478', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12477', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12476', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12475', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12474', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12472', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12473', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12471', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12470', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12469', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12468', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12466', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12467', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12465', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12463', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12464', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12462', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12461', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12460', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12459', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12458', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12457', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12456', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12455', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12454', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12453', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12452', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12451', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12450', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12449', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12448', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12447', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12446', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12444', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12445', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12443', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12442', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12440', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12441', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12439', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12438', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12436', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12437', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12435', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12434', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12433', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12432', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12431', 'http://code.ccapedu.com:80/app/book/student/weixin/resource/index/wxBookResourceIndex/oRSVkv4TaKdwBbNf9eC-Gycdgh2w/wx7e5edfb7190e963f/485?nickname=&resourceType=5&resourceId=12430']
names = ['钻天杨（李先源）', '紫羊蹄甲（李先源）', '紫藤（李先源）', '紫荆（李先源）', '梓树（李先源）', '栀子（李先源）', '珍珠绣线菊（李先源）', '樟树（李先源）', '云南山茶（李先源）', '玉兰（李先源）', '榆树（李先源）', '油松（李先源）', '银杏（李先源）', '叶子花（李先源）', '银桦（李先源）', '洋常春藤（李先源）', '野蔷薇（李先源）', '雪松（李先源）', '小叶女贞（李先源）', '孝顺竹（李先源）', '现代月季（李先源）', '西府海棠和垂丝海棠（李先源）', '无患子（李先源）', '乌桕（李先源）', '猬实（李先源）', '贴梗海棠和木瓜（李先源）', '桃（李先源）', '苏铁（李先源）', '水杉（李先源）', '深山含笑（李先源）', '杉木（李先源）', '山茶（李先源）', '沙梨（李先源）', '桑树和鸡桑（李先源）', '三角槭（李先源）', '三尖杉（李先源）', '软枝黄蝉（李先源）', '榕树（李先源）', '日本晚樱（李先源）', '日本珊瑚树（李先源）', '炮仗花（李先源）', '爬山虎和美国地锦（李先源）', '女贞（李先源）', '南洋杉和大叶南洋杉（李先源）', '南天竹（李先源）', '木香（李先源）', '木绣球（李先源）', '木兰科几属区别（李先源）', '木荷（李先源）', '茉莉（李先源）', '梅（郑丽）', '玫瑰（李先源）', '马缨丹（李先源）', '马尾松（李先源）', '麻叶绣线菊（李先源）', '络石（李先源）', '罗汉松（李先源）', '罗汉柏（李先源）', '栾树和复羽叶栾树（李先源）', '龙柏（李先源）', '龙牙花（李先源）', '六月雪（李先源）', '柳杉（李先源）', '连翘（李先源）', '李和紫叶李（李先源）', '榔榆（李先源）', '蓝花楹（李先源）', '蜡梅（李先源）', '九里香（李先源）', '锦带花和海仙花（李先源）', '金钟花（李先源）', '金银花和金银木（李先源）', '金钱松（李先源）', '接骨木（李先源）', '金花茶（李先源）', '假连翘（李先源）', '夹竹桃（李先源）', '檵木（李先源）', '鸡爪槭（李先源）', '火棘（李先源）', '鸡蛋花（李先源）', '黄金间碧玉（李先源）', '黄葛树（李先源）', '黄花夹竹桃（李先源）', '黄蝉（李先源）', '槐树（李先源）', '华山松（李先源）', '蝴蝶戏珠（李先源）', '厚皮香（李先源）', '红千层（李先源）', '红豆杉（李先源）', '合欢（李先源）', '旱柳（李先源）', '桂花（李先源）', '枸骨（李先源）', '扶芳藤（李先源）', '佛肚竹（李先源）', '凤尾兰（李先源）', '凤凰木（李先源）', '枫香（李先源）', '粉花绣线菊（李先源）', '菲白竹（李先源）', '榧树（李先源）', '鹅掌楸和北美鹅掌楸（李先源）', '冬青（李先源）', '东京樱花（李先源）', '冬红（李先源）', '棣棠（李先源）', '灯台树（李先源）', '刺槐（李先源）', '刺桐（李先源）', '垂柳（李先源）', '池杉（李先源）', '侧柏（李先源）', '白皮松（李先源）', '白鹃梅（李先源）', '八仙花（李先源）']
dict_list = []

num = len(hrefs)
# n = num//100
for i in range(num):
    res = requests.post('http://code.ccapedu.com//external/books/bookResource/getBookResourceByPath.do',
                        data={'bookResourceId': int(hrefs[i][-5:])}).json()
    url = 'http://118.190.145.95:80/srv/' + res['data']['bookResource']['path']
    dict_list.append({names[i].strip('（李先源）')+'.pdf': url})

def save(d):
    if not os.path.exists(list(d.keys())[0]):
        with open(list(d.keys())[0], 'wb') as f:
            f.write(requests.get(list(d.values())[0]).content)
            tq.update(1)
            # if divmod(i, n) == 0:
            #     stdout.write('\r下载进度 %s| %s篇/%s' % (i//n*'▉', i, num))

def mypool(pool_num, func, args):
    """
    创建线程池下载

    :param pool_num: 线程数
    :param func: 函数
    :param args: 提供给函数的参数
    :return: 无
    """
    pool = ThreadPool(pool_num)  # 线程池的个数，也就是同时下载的图片张数
    request = makeRequests(func, args)
    [pool.putRequest(req) for req in request]
    pool.wait()
    print('进程结束！')

with tqdm(total=num, desc='下载进度', ncols=70, unit='篇') as tq:
    mypool(30, save, dict_list)
