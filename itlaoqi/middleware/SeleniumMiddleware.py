import logging
import time

from scrapy.http import HtmlResponse
from selenium.common.exceptions import TimeoutException


class SeleniumMiddleware(object):

    def process_request(self, request, spider):
        logging.info('******ChromeDriver is Starting******')
        try:
            spider.browser.get(request.url)
            time.sleep(5)
            return HtmlResponse(url=request.url, body=spider.browser.page_source, request=request, encoding='utf-8',
                                status=200)
        except TimeoutException:
            return HtmlResponse(url=request.url, status=500, request=request)
