import scrapy, os


class MessageSpider(scrapy.Spider):
    name = 'message'
    allowed_domains = ['4qx.net']
    start_urls = ['http://www.4qx.net/DuanXin_DaQuan.php']
    n = 0

    def parse(self, response):
        kind_names = response.css('.main_lix5 ul a::text').getall()
        kind_urls = response.css('.main_lix5 ul a::attr(href)').getall()

        if not os.path.exists('短信'):
            os.mkdir('短信')
        os.chdir('短信')
        for i in range(len(kind_names)):
            with open(kind_names[i]+'.txt', 'w'):
                pass
            url = response.urljoin(kind_urls[i])
            yield scrapy.Request(url, callback=self.parse_detail, meta={'name': kind_names[i]+'.txt'})

    def parse_detail(self, response):
        msgs = response.css('.main_duanxin_1 p::text').getall()
        if msgs:
            print('抓取到第 %s 篇' % self.n)
        self.n += 1
        name = response.meta['name']
        with open(name, 'a') as f:
            for msg in msgs:
                f.write(msg + '\n\n')
        next_pages = response.css('pagecss a::attr(href)')[:-1]
        yield from response.follow_all(next_pages, self.parse_detail)
