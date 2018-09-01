from scrapy_plus.core.engine import Engine
from project_dir.spiders.baidu import BaiduSpider
from project_dir.spiders.douban import DoubanSpider
from project_dir.pipelines import BaiduPipeline,DoubanPipeline
from project_dir.middlewares.downloader_middlewares import BaiduDownloaderMiddleware
from project_dir.middlewares.downloader_middlewares import DoubanDownloaderMiddleware
from project_dir.middlewares.spider_middlewares import BaiduSpiderMiddleware
from project_dir.middlewares.spider_middlewares import DoubanSpiderMiddleware
if __name__ == '__main__':

    # 创建百度爬虫
    baidu_spider = BaiduSpider()

    # 2.1.1-3创建豆瓣爬虫
    douban_spider = DoubanSpider()
    # 2.2-1 准备一个爬虫的字典
    # 2.3-5:把原来写死的名称换成爬虫中的名称
    spiders ={
        BaiduSpider.name:baidu_spider,
        DoubanSpider.name:douban_spider
    }
    # 2.3-6:创建管道的列表，传入到引擎中去
    pipelines =[BaiduPipeline(),DoubanPipeline()]

    # 2.4-2:定义爬虫中间列表和下载器中间件列表
    spider_middlewares =[
        BaiduSpiderMiddleware(),
        DoubanSpiderMiddleware(),
    ]

    downloader_middlewares =[
        BaiduDownloaderMiddleware(),
        DoubanDownloaderMiddleware()
    ]
    # 创建引擎对象
    engine = Engine(spiders,pipelines,spider_middlewares,downloader_middlewares)

    # engine = Engine()
    engine.start()



