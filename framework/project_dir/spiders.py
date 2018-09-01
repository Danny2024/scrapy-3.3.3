"""项目中的爬虫"""
from scrapy_plus.core.spider import Spider
from scrapy_plus.items import Item
from scrapy_plus.http.request import Request
class BaiduSpider(Spider):
    # 2.0.2-1:定义起始URL
    start_urls = ['https://www.baidu.com','http://www.itcast.cn']


class DoubanSpider(Spider):
    start_urls = ['https://movie.douban.com/top250',]


    # 2.1.2-1 解析函数返回多个数据
    def parse(self,response):

        a_s = response.xpath('//*[@id="content"]/div/div[1]/ol/li/div/div[2]/div[1]/a')
        for a in a_s:
            data = {}
            data['movie_name'] = a.xpath('./span[1]/text()')[0]
            data['movie_url'] = a.xpath('./@href')[0]
            # print(data)
            # yield Item(data)
            yield Request(data['movie_url'],callback=self.parse_detail,meta={'data':data})


    def parse_detail(self,response):
        data =response.meta['data']
        data['movie_length'] = response.xpath('//span[@property="v:runtime"]/text()')

        return Item(data)