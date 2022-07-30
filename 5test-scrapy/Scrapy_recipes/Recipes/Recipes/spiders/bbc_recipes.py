import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BbcRecipesSpider(CrawlSpider):
    name = 'bbc_recipes'
    allowed_domains = ['www.bbcgoodfood.com']
    start_urls = ['http://www.bbcgoodfood.com/']

    # TODO: Add a new rule 4 crawl everything of the page
    rules = (
        Rule(LinkExtractor(allow=(r'collection',r'category'))),
        Rule(LinkExtractor(allow=r'recipes/',deny=(r'collection',r'category')), callback='parse_recipe', follow=True),
    )

    def parse_recipe(self, response):
        item = {}
        item['title'] = response.css('div.headline h1::text').get()
        recipe = response.css('div.recipe__instructions').get()
        item['ingredients'] = recipe.css('section.recipe__ingredients li::text').getall()
        item['instrucctions'] = recipe.css('section.recipe__method-steps li ::text').getall()
        return item