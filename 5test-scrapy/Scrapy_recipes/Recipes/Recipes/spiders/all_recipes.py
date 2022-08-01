import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class AllRecipesSpider(CrawlSpider):
    name = 'all_recipes'
    allowed_domains = ['www.allrecipes.com']
    start_urls = ['http://www.allrecipes.com/']

    rules = (
        Rule(LinkExtractor(allow=r'recipe/'), callback='parse_recipe', follow=True),
    )

    def parse_recipe(self, response):
        item = {}
        item['title'] = response.css('div.main-header div.intro ::text').get()
        recipe = response.css('div.recipe__instructions').get()
        unclean_ingredients = response.css('ul.ingredients-section ::text').getall()
        item['ingredients'] = list(filter(lambda x: x != ' ', unclean_ingredients))

        unclean_instructions = response.css('section.recipe-instructions ::text').getall()
        item['instructions'] = list(filter(lambda x: x != ' ', unclean_instructions))
        return item

    def parse_item(self, response):
        item = {}
        item[''] = response.xpath('//input[@id="sid"]/@value').get()
        #item['name'] = response.xpath('//div[@id="name"]').get()
        #item['description'] = response.xpath('//div[@id="description"]').get()
        return item
