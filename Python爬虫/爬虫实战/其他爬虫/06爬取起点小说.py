import requests, sys
from bs4 import BeautifulSoup


class downloader(object):
    def __init__(self, target):  # 初始化
        self.target = target
        self.chapterNames = []
        self.chapterHrefs = []
        self.chapterNum = 0
        self.session = requests.Session()

    def GetChapterInfo(self):  # 获取章节名称和链接
        req = self.session.get(url=self.target)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        html = req.text
        bf = BeautifulSoup(html, "html.parser")
        catalogDiv = bf.find('div', class_='catalog-content-wrap', id='j-catalogWrap')
        volumeWrapDiv = catalogDiv.find('div', class_='volume-wrap')
        volumeDivs = volumeWrapDiv.find_all('div', class_='volume')

        for volumeDiv in volumeDivs:
            aList = volumeDiv.find_all('a')
            for a in aList:
                chapterName = a.string
                chapterHref = a.get('href')
                self.chapterNames.append(chapterName)
                self.chapterHrefs.append('https:' + chapterHref)
            self.chapterNum += len(aList)

    def GetChapterContent(self, chapterHref):  # 获取章节内容
        req = self.session.get(url=chapterHref)
        req.raise_for_status()
        req.encoding = req.apparent_encoding
        html = req.text
        bf = BeautifulSoup(html, "html.parser")
        mainTextWrapDiv = bf.find('div', class_='main-text-wrap')
        readContentDiv = mainTextWrapDiv.find('div', class_='read-content j_readContent')
        readContent = readContentDiv.find_all('span', class_='content-wrap')
        textContent = ''
        if not readContent:
            textContent = readContentDiv.text.replace('<p>', '\r\n').replace('</p>', '')
        else:
            for content in readContent:
                if content.string == '':
                    print('error format')
                else:
                    textContent += content.string + '\r\n'
        return textContent

    def writer(self, path, name='', content=''):
        write_flag = True
        with open(path, 'a', encoding='utf-8') as f:  # a模式意为向同名文件尾增加文本
            if name is None:
                name = ''
            if content is None:
                content = ''
            f.write(name + '\r\n')
            f.writelines(content)
            f.write('\r\n')


if __name__ == '__main__':  # 执行层
    target = 'https://book.qidian.com/info/1024995653#Catalog'
    dlObj = downloader(target)
    dlObj.GetChapterInfo()
    print('开始下载：')
    for i in range(dlObj.chapterNum):
        try:
            dlObj.writer(f'{i}{dlObj.chapterNames[i]}.txt', dlObj.chapterNames[i], dlObj.GetChapterContent(dlObj.chapterHrefs[i]))
        except Exception:
            print('下载出错，已跳过')
            pass
        sys.stdout.write("  已下载:%.3f%%" % float(i / dlObj.chapterNum) + '\r')
        sys.stdout.flush()
    print('下载完成')
