import scrapy

class TextingSpider(scrapy.Spider):
    name = 'textingspider'
    start_urls = ['http://www.opentextingonline.com/textspeak.aspx']

    def parse(self, response):
        for row in response.css('tr[itemprop="itemListElement"]'):
            [text, translation] = row.css('td::text').extract()
            yield {'text' : text, 'translation' : translation}

