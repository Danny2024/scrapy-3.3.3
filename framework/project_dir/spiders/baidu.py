from scrapy_plus.core.spider import Spider

class BaiduSpider(Spider):
    # 2.3-3:增加name属性
    name = 'baidu'
    # 2.0.2-1:定义起始URL
    start_urls = ['https://www.baidu.com','http://www.itcast.cn']
