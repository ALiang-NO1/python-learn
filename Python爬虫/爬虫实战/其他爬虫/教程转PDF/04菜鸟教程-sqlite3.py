# encoding:utf8
import pdfkit, requests, asyncio
from bs4 import BeautifulSoup

"""不能使用协程同时爬取，因为这样目录会乱！"""

tmp = "<html><head><meta charset='utf8'><link rel='stylesheet' href='https://www.runoob.com/wp-content/themes/runoob/style.css?v=1.157'></head><body>{}</body></html>"
text = ''
url_list = []
home_url = 'https://www.runoob.com'
res = requests.get('https://www.runoob.com/sqlite/sqlite-commands.html').text
soup = BeautifulSoup(res, 'lxml')
for a in soup.find_all('a', target='_top'):
    try:
        if not a:
            continue
        if not a['href']:
            continue
        url_list.append(home_url+a['href'])
    except Exception as e:
        print('e:', e)
        continue
# print(url_list)

def get_content(url):  # async
    global text
    res = requests.get(url).text
    soup = BeautifulSoup(res, 'lxml')
    text += str(soup.find('div', class_='article-intro'))
for url in url_list:
    get_content(url)
# loop = asyncio.get_event_loop()
# tasks = [get_content(url) for url in url_list]
# loop.run_until_complete(asyncio.wait(tasks))
# loop.close()
print('开始转PDF...')
pdfkit.from_string(tmp.format(text), 'sqlite3参考手册.pdf')
print('完成！')