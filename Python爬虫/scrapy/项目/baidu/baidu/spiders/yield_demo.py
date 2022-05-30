import scrapy


class YieldDemoSpider(scrapy.Spider):
    name = 'yield_demo'
    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com/']

    def parse_author(self, response):
        def extract_with_css(query):  # 从CSS查询中提取和清理数据
            return response.css(query).get(default='').strip()

        print({
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'bio': extract_with_css('.author-description::text'),
        })

    def parse(self, response):
        author_page_links = response.css('.author + a')  # follow_all() 处理所有链接
        yield from response.follow_all(author_page_links, self.parse_author)  # 作者跳转 -> 作者简介 -> 生产信息（文本）

        pagination_links = response.css('li.next a')
        yield from response.follow_all(pagination_links, self.parse)  # 追踪下一页
