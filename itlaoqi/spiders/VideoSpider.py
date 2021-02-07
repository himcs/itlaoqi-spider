import re

import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from itlaoqi.service.ChapterService import ChapterService


class VideoSpider(scrapy.Spider):
    name = "video"

    custom_settings = {
        'DOWNLOADER_MIDDLEWARES': {
            'itlaoqi.middleware.SeleniumMiddleware.SeleniumMiddleware': 521,
        }
        ,
        'ITEM_PIPELINES': {
            'itlaoqi.pipeline.RabbitPipeline.RabbitPipeline': 300,
        }
    }

    def __init__(self):
        chrome_options = Options()
        prefs = {
            'profile.default_content_setting_values': {
                'images': 2,  # 禁用图片的加载
                # 'javascript': 2  # 禁用js，可能会导致通过js加载的互动数抓取失效
            }
        }
        chrome_options.add_experimental_option("prefs", prefs)
        # 无头浏览器设置
        chrome_options.add_argument("--headless")
        chrome_options.add_argument("--disable-gpu")
        self.browser = webdriver.Chrome(executable_path="D:\driver\chromedriver.exe", chrome_options=chrome_options)

    def start_requests(self):
        result = ChapterService().get_all()
        for catalogue in result:
            print(catalogue)
            yield scrapy.Request(url=catalogue['url'], callback=self.parse, meta=catalogue)

    def parse(self, response):
        matchObj = re.search(r'cover: "(.*)"', response.text, re.M)
        if matchObj:
            img = matchObj[1]
        else:
            img = ''
        video_url = response.css('video').xpath('@src').get()
        if not video_url:
            video_url = ''
        id = response.meta['id']
        yield {"exchange": "EXCAHNGE_VIDEO",
               "id": str(id),
               "img": str(img),
               "video_url": str(video_url),
               }

    def closed(self, spider):
        print('爬虫结束')
        self.browser.quit()
