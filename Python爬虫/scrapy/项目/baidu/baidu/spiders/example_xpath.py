import scrapy


class ExampleXpathSpider(scrapy.Spider):
    name = 'example_xpath'
    allowed_domains = ['exercise.kingname.info']
    start_urls = ['http://exercise.kingname.info/exercise_xpath_1.html']

    def parse(self, response):
        name_list = response.xpath('//ul[@class="item"]/li[@class="name"]/text()').extract()
        price_list = response.xpath('//ul[@class="item"]/li[@class="price"]/text()').extract()
        for i in range(len(name_list)):
            print('%s的价格是：%s' % (name_list[i], price_list[i]))
        print('-'*20)
        name = response.xpath('//ul[@class="item"]/li[@class="name"]/text()').extract_first()
        price = response.xpath('//ul[@class="item"]/li[@class="price"]/text()').extract()[0]
        print(name, price)
