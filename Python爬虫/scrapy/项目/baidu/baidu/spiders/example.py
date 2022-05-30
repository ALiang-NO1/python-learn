import scrapy


class ExampleSpider(scrapy.Spider):
    name = 'example'
    allowed_domains = ['baidu.com']
    start_urls = ['http://baidu.com/']

    def parse(self, response):
        print(response.body.decode())
