from urllib.parse import urljoin
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class UsiNewsSpider(CrawlSpider):
    name = 'Usi_news'
    allowed_domains = ['www.usi.ch']
    start_urls = ['https://www.usi.ch/en/news-events/news']

    rules = (
        Rule(LinkExtractor(allow=r'en/news-events/news\?page=[1-5]'), callback='parse_News', follow=True),
    )

    def parse_News(self, response):
        usi_news = []
        for n in response.css('div.news'):
            news = {}
            news['title'] = n.css('a h3::text').get()
            url = n.css('a::attr(href)').get()
            news['link'] = response.urljoin(url)
            news = response.follow(url, self.parse_inside_a_new, cb_kwargs=dict(item=news))
            usi_news.append(news)
        return usi_news

    def parse_inside_a_new(self, response, item):
        item['description'] = response.css('div.section_item div.text_container p ::text').getall()
        return item
