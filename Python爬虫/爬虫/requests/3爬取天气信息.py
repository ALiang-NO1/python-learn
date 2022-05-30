import requests
from bs4 import BeautifulSoup

qy = open('E:/python文档/my_py/爬虫/07天气信息.txt', mode='a', encoding='utf-8')
res = requests.get('http://www.weather.com.cn/weather15d/101190401.shtml')
res.encoding = 'utf-8'
html = res.text
soup = BeautifulSoup(html, 'html.parser')    # 解析文档
weathers = soup.find(id="15d", class_="c15d").find('ul', class_="t clearfix").find_all('li')
for weather in weathers:
    weather_date = weather.find('span', class_="time")
    weather_wea = weather.find('span', class_="wea")
    weather_tem = weather.find('span', class_="tem")
    weather_wind = weather.find('span', class_="wind")
    weather_wind1 = weather.find('span', class_="wind1")
    result = '日期：'+weather_date.text, '天气：'+weather_wea.text, '温度：'+weather_tem.text, \
             '风力：'+weather_wind.text+weather_wind1.text
    print(result)   # 输出
    print(result,  file=qy)      # 保存到文档中
qy.close()