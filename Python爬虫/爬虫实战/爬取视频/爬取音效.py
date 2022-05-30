import requests
import time
import os
import threadpool
from lxml import etree
from selenium import webdriver

keys = ["jiaotong2", "shenghuo35", "ruanjian2", "dongwu9", "renwu9", "youxi8"]
i = 1
for page in range(2, 10):
    print(f"-----------当前正在爬取第{page}页-----------")
    url = "http://www.1ppt.com/music/renwu/music_%s.html" % page
    dir_path = r"F:\music\音效\renwu"
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    dict_list = []

    # html = etree.HTML(requests.get(url).text)
    # print(requests.get(url).text)
    # all_li = html.xpath('//ul[@class="tplist"]/li')
    # print("all_li", all_li)

    chrome_driver = r"D:\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=chrome_driver, options=options)
    driver.get(url)
    time.sleep(3)
    html = etree.HTML(driver.page_source)
    all_li = html.xpath('//ul[@class="tplist"]/li')
    for li in all_li:
        name = li.xpath("./a/img/@alt")[0]
        src = li.xpath("./div/audio/source/@src")[0]
        dict = {'name': name, 'src': src}
        dict_list.append(dict)

    def spider(dict):
        global i
        os.chdir(dir_path)
        file_name = dict['name'] + '.mp3'
        if not os.path.exists(file_name):
            with open(file_name, 'wb') as f:
                f.write(requests.get(dict['src']).content)
                print(f"{i}.{file_name}保存成功！")
        i += 1

    def main(function, arg):
        pool = threadpool.ThreadPool(25)
        request = threadpool.makeRequests(function, arg)
        [pool.putRequest(req) for req in request]
        pool.wait()

    main(spider, dict_list)