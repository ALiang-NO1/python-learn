import pdfkit
import requests
from bs4 import BeautifulSoup

res = requests.get('https://v3.bootcss.com/components')  # 这里修改网址
res.encoding = 'utf8'
soup = BeautifulSoup(res.text, 'lxml')
content = soup.find('div', class_='col-md-9')  # 这里修改 xpath
link = 'https://fastly.jsdelivr.net/npm/@bootcss/v3.bootcss.com@1.0.30/assets/css/docs.min.css'  # 这里修改样式网址

# path_wk = r'D:\program\wkhtmltox\bin'  # wkhtmltopdf安装位置
# config = pdfkit.configuration(wkhtmltopdf=path_wk)
tpl = '<html><head><meta charset=utf8><link href=%s rel="styleSheet"></head><body>{}</body></html>' % link
pdfkit.from_string(tpl.format(str(content)), r'E:\bootstrap-progress.pdf')  # , configuration=config
