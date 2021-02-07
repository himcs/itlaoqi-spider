import scrapy
import re
from itlaoqi.service.CatalogueService import CatalogueService


class ChapterSpider(scrapy.Spider):
    name = "chapter"

    custom_settings = {'ITEM_PIPELINES': {
        'itlaoqi.pipeline.RabbitPipeline.RabbitPipeline': 300,
    }}

    def start_requests(self):
        result = CatalogueService().get_all()
        for catalogue in result:
            print(catalogue)
            yield scrapy.Request(url=catalogue['url'], callback=self.parse, meta=catalogue)

    def parse(self, response):
        order = 0
        for t in response.css('.col-8 a.list-group-item'):
            url = t.xpath('@href').get().strip()
            name = t.xpath('text()')[1].get().strip()
            ttime = t.css('span:last-child').xpath('text()').get()
            num = re.findall(r'\d+', ttime)
            if len(num) > 0:
                time = num[0].strip()
            else:
                time = 0
            cid = response.meta['id']
            order = order + 1
            yield {"exchange": "EXCAHNGE_CHAPTER",
                   "name": name,
                   "url": 'https://www.itlaoqi.com' + url,
                   "sort": str(order),
                   "time": str(time),
                   "cid": str(cid)
                   }
