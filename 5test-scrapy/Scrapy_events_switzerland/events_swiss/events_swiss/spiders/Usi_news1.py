import scrapy


class UsiNews1Spider(scrapy.Spider):
    name = 'Usi_news1'
    allowed_domains = ['www.usi.ch']
    start_urls = ['http://www.usi.ch/']

    def parse(self, response):
        pass
