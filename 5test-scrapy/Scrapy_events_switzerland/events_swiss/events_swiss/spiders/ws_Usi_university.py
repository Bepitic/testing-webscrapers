import scrapy

class Usi_events(scrapy.Spider):
    # webpage - english https://www.usi.ch/en
    # https://www.usi.ch/en/news-events/events
    name = "USI_events"
    start_urls = ['https://www.usi.ch/en/news-events/events']

    def parse(self, response):
        page = response.url.split("/")[-4]
        # title = response.xpath("//div[@class='date_container']//a/text()").get()
        # print(filename)
        for event in response.css('div.date_container'):
            yield {
                'title' : event.css("a::text").get(),
                'day' : event.css("div.day::text").get(),
                'month' : event.css("div.month::text").get(),
                'year' : event.css("div.year::text").get(),
                'link' : response.urljoin(event.css("a::attr(href)").get()),
            }
        next_page = response.css('li.pager-next a::attr(href)').get()
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)