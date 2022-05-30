import requests
import parsel

url1 = "http://www.huya.com/g/2168"
headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) '
                         'Chrome/70.0.3538.25 Safari/537.36 Core/1.70.3775.400 QQBrowser/10.6.4209.400'}
response = requests.get(url1, headers=headers)
# print(request.text)

selector = parsel.Selector(response.text)
urls = selector.css('.live-list .game-live-item a img::attr(data-original)').getall()
titles = selector.css('.live-list .game-live-item a img::attr(title)').getall()
print(urls)
print(type(titles))
info_date = zip(urls, titles)
for i in info_date:
    img_url = i[0].split('?')[0]
    title = i[1][:-3]
    img_url_response = requests.get(img_url, headers=headers)
    path = "F:\img\虎牙主播\\" + title + ".jpg"
    with open(path, 'wb') as f:
        f.write(img_url_response.content)
        print(title)