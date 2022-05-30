import scrapy


class YeildTestSpider(scrapy.Spider):
    name = 'yeild_test'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/page/1']

    def parse(self, response):
        for quote in response.css('div.quote'):
            print({
                'text': quote.css('span.text::text').get(),  # 返回第一个
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),  # 返回列表
            })
        next_page = response.css('li.next a::attr(href)').get()
        if next_page is not None:  # 继续爬取一页
            # yield response.follow(next_page, callback=self.parse)  # 无需拼接url
            next_page = response.urljoin(next_page)  # 拼接url
            yield scrapy.Request(next_page, callback=self.parse)
