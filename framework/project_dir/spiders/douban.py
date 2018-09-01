"""项目中的爬虫"""
from scrapy_plus.core.spider import Spider
from scrapy_plus.items import Item
from scrapy_plus.http.request import Request

class DoubanSpider(Spider):
    # 2.3-3:增加name属性
    name = 'douban'
    start_urls = ['https://movie.douban.com/top250']
    headers = {
        'Cookie':'bid=WfrYJ9WpAwk; ll="118281"; __yadk_uid=2ewLmX7OPUiqswLUbtw9Z17452Cwqi9h; _vwo_uuid_v2=D940036227E45540134BB73C8740ADEE8|6c244493546a9daaeb5772d92e27f5d2; viewed="3634993"; gr_user_id=f8399021-da22-4233-adaf-1f0e58561ebb; __utmz=223695111.1532268257.4.3.utmcsr=bing|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); douban-fav-remind=1; __utmz=30149280.1532590529.11.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); ap=1; ct=y; ap_v=1,6.0; ap_6_0_1=1; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1535028023%2C%22https%3A%2F%2Fwww.bing.com%2F%22%5D; _pk_id.100001.4cf6=6bdb2eaa61342b48.1527847714.9.1535028023.1533738664.; _pk_ses.100001.4cf6=*; __utma=30149280.1652869297.1527847712.1533392195.1535028023.13; __utmb=30149280.0.10.1535028023; __utmc=30149280; __utma=223695111.1253550479.1527847712.1533392195.1535028023.6; __utmc=223695111; __utmt=1; __utmb=223695111.1.10.1535028023'
    }
    def start_requests(self):
        for start_url in self.start_urls:
            yield Request(start_url, headers=self.headers)

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
        data = response.meta['data']
        data['movie_length'] = response.xpath('//span[@property="v:runtime"]/text()')

        return Item(data)