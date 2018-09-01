import time

from scrapy_plus.core.spider import Spider
from scrapy_plus.http.request import Request
from scrapy_plus.items import Item

class SinaSpider(Spider):
    name = 'sina'

    def start_requests(self):
        url = 'http://roll.news.sina.com.cn/interface/rollnews_ch_out_interface.php'
        while True:
            yield Request(url, dont_filter =True)
            # 一定等待在yield后面
            time.sleep(2)
    def parse(self,response):
        # 设置编码方式为GBK
        response.encoding = 'GBK'

        # result=response.re_find_all('{channel\s*:\s*{title\s*:\s*"(.+?)",')
        print(response.url)
        return Item(response.url)