import re
import os
import sqlite3
import requests
import pymysql
import hashlib
from bs4 import BeautifulSoup

def verify_update(html):
    """ 这个函数需要导入hashlib模块，然后创建一个md5的对象，把当前页面的信息传入，通过使用updata()方法对传入的数据进行MD5运算。
        然后使用if语句判断文件是否存在，如果存在就读取其中的MD5码，再通过判断两次的MD5码是否相同，如果一样就表示没有更新，
        反之则进行了更新，把新的MD5码传到文件中。"""
    md5 = hashlib.md5()   # md5.new()
    md5.update(html.encode(encoding='utf-8'))   # Unicode 对象哈希化之前必须编码
    md5code = md5.hexdigest()  # 转为32位字符串
    old_html = ''
    html_name = 'gp.txt'
    if os.path.exists(html_name):
        with open(html_name, 'r', encoding='utf-8') as f:
            old_html = f.read()
    if md5code == old_html:
        print('数据未更新')
        return False
    else:
        with open(html_name, 'w', encoding='utf-8') as f:
            f.write(md5code)
        print('数据更新了')
        return True

qy = open('02豆瓣信息.txt', mode='w', encoding='utf-8')    # 这里是要存入的文件目录
for i in range(2):
    headers = {    # 这里模拟浏览器进行访问
        'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/52.0.2743.82 Safari/537.36', 'Host': 'movie.douban.com'}
    res = 'https://movie.douban.com/top250?start='+str(1)    # 25页
    r = requests.get(res, headers=headers, timeout=10)    # 设置超时时间
    soup = BeautifulSoup(r.text, "lxml")    # 设置解析方式, 也可以使用其他方式。
    div_list = soup.find_all('div', class_='item')      # 单个电影的全部框架（信息）
    movies = []     # 首先定义一个列表来存储所有信息
    for each in div_list:
        movie = {}

        # title的位置是名为‘hd’的‘div’下的第一个‘a’中的第一个‘span’，因此我们可以通过下面代码来锁定每一个电影的名字
        moviename = each.find('div', class_='hd').a.span.text.strip()   # 获取电影名并除去首尾空格
        movie['title'] = moviename      # 将名字放到一个字典中。

        rank = each.find('div', class_='pic').em.text.strip()   # 获取电影的排名
        movie['rank'] = rank

        info = each.find('div', class_='bd').p.text.strip()
        info = info.replace('\\n', "")
        info = info.replace(" ", "")
        # info = info.replace("\\xa0", "")
        director = re.findall(r'[导演:].+[主演:]', info)[0]
        director = director[3:len(director) - 6]
        movie['director'] = director

        release_date = re.findall(r'[0-9]{4}', info)[0]     # 获取发行日期
        movie['release_date'] = release_date
        plot = re.findall(r'[0-9]*[/].+[/].+', info)[0]     # 场地及类型
        plot = plot[1:]
        plot = plot[plot.index('/') + 1:]
        movie['plot'] = plot

        star = each.find('div', class_='star')
        star = star.find('span', class_='rating_num').text.strip()      # 获取评分
        movie['star'] = star

        quote = each.find('span', class_='inq').string
        movie['quote'] = quote      # 语录（电影说明）

        movies.append(movie)
        print(movie, file=qy)    # 保存到文件中

    # con = pymysql.connect(host='localhost' + user='root', password='123456', database='python', charset='utf8', port=3306)
    con = sqlite3.connect('dbinfo.db')
    print('连接成功->')
    cursor = con.cursor()    # 创建一个游标
    print('开始创建表->')
    cursor.execute("""create table douban(
                      title char(40),
                      ranks char(40), 
                      director char(40), 
                      release_date char(40), 
                      plot char(100), 
                      star char(40), 
                      quote char(80))""")
    print('完成表的创建, 开始插入数据->')    # 下面开始插入数据
    for i in movies:
        cursor.execute("insert into douban(title, ranks, director, release_date, plot, star, quote) "
                       "values(%s, %s, %s, %s, %s, %s, %s)", (i['title'], i['rank'], i['director'],
                       i['release_date'], i['plot'], i['star'], i['quote']))
    print('插入数据完成')
    cursor.close()
    con.commit()
    con.close()