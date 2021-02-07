import scrapy


class CatalogueSpider(scrapy.Spider):
    name = "catalogue"

    custom_settings = {'ITEM_PIPELINES': {
        'itlaoqi.pipeline.RabbitPipeline.RabbitPipeline': 300,
    }}

    def start_requests(self):
        urls = [
            'https://www.itlaoqi.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        for a in response.css('.series')[1:]:
            img = a.css('div > a > img').xpath('@alt').get()
            b = a.css('div > div.card-title > a')
            url = b.xpath('@href').get()
            name = b.xpath('text()').get()
            yield {"exchange": "EXCAHNGE_CATALOGUE", "name": name, "url": 'https://www.itlaoqi.com' + url, "img": img}
