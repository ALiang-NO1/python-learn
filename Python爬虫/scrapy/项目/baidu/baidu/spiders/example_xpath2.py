import scrapy


class ExampleXpath2Spider(scrapy.Spider):
    name = 'example_xpath2'
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['http://exercise.kingname.info/exercise_xpath_2.html']

    def parse(self, response):
        for ul in response.xpath('//ul[@class="name"]'):
            name = ul.xpath('//li[@class="name"]/text()').extract()
            price = ul.xpath('//li[@class="price"]/text()').extract()
            name = name[0] if name else 'N/A'
            price = price[0] if price else 'N/A'
            print('名称：%s，价格：%s' % (name, price))
