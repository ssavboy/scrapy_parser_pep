import scrapy

from pep_parse.items import PepParseItem


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = ['https://peps.python.org/']

    def parse(self, response):
        for link in response.css('section#numerical-index td a::attr(href)'):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        title = response.css('h1.page-title ::text').get().split(' – ')
        yield PepParseItem({
            'number': title[0],
            'name': title[1],
            'status': response.css('abbr::text').get(),
        })
