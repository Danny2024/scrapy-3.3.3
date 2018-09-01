# 默认的配置
import logging
DEFAULT_LOG_LEVEL = logging.INFO    # 默认等级
DEFAULT_LOG_FMT = '%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s: %(message)s'   # 默认日志格式
DEFUALT_LOG_DATEFMT = '%Y-%m-%d %H:%M:%S'  # 默认时间格式
DEFAULT_LOG_FILENAME = 'log.log'    # 默认日志文件名称
# 2.5-3:在框架默认配置中增加［爬虫，管道，中间件，目的是为了后续携带码方便
SPIDERS =[]

PIPELINES = []

DOWNLOADER_MIDDLEWARES =[]

SPIDER_MIDDLEWARES =[]

# 3.0.2--1.修改 default_settings.py增加异步任务个数配置
ASYNC_COUNT = 5

# 3.1-1 异步类型：thread(线程),coroutine(协程)
ASYNC_TYPE = 'coroutine'

# 3.2.0-1: 增加redis相关配置
# 队列在redis中的key
REDIS_QUEUE_NAME = 'scrapy_plus_queue_key'

# 去重容器set集合
REDIS_SET_NAME = 'scrapy_plus_set_key'

REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
REDIS_DB = 0

# 配置要不要开启分布式，也就是　是不是要对调度相关的数据进行持久化
SCHEDULE_PERSIST = False

# 要不要对指纹进行持久化，即要不要开启断点续爬
FP_PERSIST = True

