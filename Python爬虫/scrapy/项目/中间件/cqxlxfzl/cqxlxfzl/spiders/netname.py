import scrapy

class NetnameSpider(scrapy.Spider):
    name = 'netname'
    allowed_domains = ['cqxlxfzl.com']  # 苍穹文章网
    start_urls = ['http://www.cqxlxfzl.com/wangmingdaquan/gexingwangming/']

    def parse_text(self, response):
        for p in response.css('#contents p'):
            name = p.xpath('//@text').get()


    def parse(self, response):
        for dl in response.css('#lieb dl'):
            title = dl.css('dt h2 a::text').get()  # 文章标题
            href = dl.css('dt h2 a::attr(href)').get()  # 跳转链接
            print(title, href)
