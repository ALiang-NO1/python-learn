import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import re
import os
from lxml import etree
from PIL import Image
from selenium.webdriver.common.keys import Keys


def rq(url):
    head = {'User-agent': 'Googlebot'}
    res = requests.get(url, headers=head)
    return res

def doc(url, filename):
    """<p class="reader-word-layer reader-word-s1-20" style="width: 2477px; height: 190px; line-height: 190px; top: 8619px; left: 2000px; z-index: 135;">app&nbsp;=&nbsp;wx.PySimpleApp()&nbsp;&nbsp;&nbsp;&nbsp;
</p>"""
    """保存word文档"""
    driver = webdriver.Chrome(r'D:\chromedriver.exe')
    driver.get(url)

    input = driver.find_element_by_class_name("cur-page")
    input.click()
    input.send_keys('19')
    input.send_keys(Keys.ENTER)
    driver.get(url)

    html = etree.HTML(driver.page_source)
    # print(driver.page_source)
    ps = ''
    for p in html.xpath('//div[@class="ie-fix"]/p/text()'):
        ps += p
    print(ps)
        # with open(filename, "w", encoding='utf-8') as f:
        #     f.write(p.get_text())
        # print("success")
doc("https://wenku.baidu.com/view/edce5f2e87c24028915fc365.html", "wx知识.txt")

def pdf(url):
    """获取pdf图片"""
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(r'D:\chromedriver.exe', options=options)
    driver.get(url)

    input = driver.find_element_by_class_name("cur-page")
    input.click()
    input.send_keys('11')
    input.send_keys(Keys.ENTER)
    driver.get(url)

    html = etree.HTML(driver.page_source)
    links = html.xpath("//div[@class='reader-pic-item']/@style")
    part = re.compile(r'url[(](.*?)[)]')
    qa = "".join(links)     # 拼接列表里的字符串
    urls = part.findall(qa)    # 获取图片链接
    print(len(urls))
    for i in range(11):
        if not os.path.exists(f'{i+1}.jpg'):
            with open(f'{i+1}.jpg', 'wb') as f:
                f.write(rq(urls[i].strip('"')).content)
                print(f'{i+1}.jpg 保存成功！')

def save_pdf():
    """保存PDF图片 """
    folderPath = "F:/TEST"
    filename = "test"
    files = os.listdir(folderPath)
    jpgFiles = []
    sources = []
    for file in files:
        if 'jpg' in file:
            jpgFiles.append(file)
    tep = []
    for i in jpgFiles:
        ex = i.split('.')
        tep.append(int(ex[0]))
    tep.sort()
    jpgFiles = [folderPath + '/' + str(i) + '.jpg' for i in tep]
    output = Image.open(jpgFiles[0])
    jpgFiles.pop(0)
    for file in jpgFiles:
        img = Image.open(file)
        img = img.convert("P")
        sources.append(img)
    output.save(f"./{filename}.pdf", "PDF", save_all=True, append_images=sources)