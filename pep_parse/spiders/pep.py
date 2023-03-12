import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = ['peps.python.org']
    start_urls = [URL.format(domain=domain) for domain in allowed_domains]

    def parse(self, response):
        for link in response.css('section#numerical-index td a::attr(href)'):
            yield response.follow(link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = response.css(
            'h1.page-title ::text').get().split(' – ')
        yield PepParseItem({
            'number': number,
            'name': name,
            'status': response.css('abbr::text').get(),
        })
