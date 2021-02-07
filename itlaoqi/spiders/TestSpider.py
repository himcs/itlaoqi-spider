import scrapy

class TestSpider(scrapy.Spider):
    name = "test"

    custom_settings = {'ITEM_PIPELINES': {
        'itlaoqi.pipeline.TestPipeline.TestPipeline': 300,
    }}

    def start_requests(self):
        urls = [
            'https://www.baidu.com/',
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        yield {"test": "a"}
        return
