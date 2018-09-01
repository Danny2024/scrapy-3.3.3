# coding:utf8

# six是一个专门用于python2和python3兼容的
import six

import hashlib
# 导入url规范化函数
from w3lib.url import canonicalize_url  # 需要在requirements.txt添加依赖
from ..utils.log import logger
from ..conf import settings

"""

调度器模块
1.缓存数据
2.请求去重

# 3.2.1
-根据配置文件．是否需要对数据（请求和指纹）进行持久化
1.如果不需要持久化，导入内存的队列和去重容器，否则导入基于redis队列和去重容器
内存版队列和redis队列一样

2.修改init方法，创建去重容器

3.修改seen_request方法，改为使用去重容器的接口
"""
# 1.如果不需要持久化，导入内存的队列和去重容器，否则导入基于redis队列和去重容器
# 内存版队列和redis队列一样
if not settings.SCHEDULE_PERSIST:
    from six.moves.queue import Queue
    from ..utils.set import NoramlFilterContainer as FilterContainer
else:
    from ..utils.queue import Queue
    from ..utils.set import RedisFilterContainer as FilterContainer


class Scheduler(object):
    def __init__(self,stats_collector):

        # 3.2.1-3: 调度器中接受统计器对象，使用统计器对象，对入对的请求数量和过滤掉的请求数量进行统计
        self.stats_collector = stats_collector

        # 准备队列，来缓存请求对象
        self.queue = Queue()
        # 2.0.2-５:统计总的请求数量
        # self.total_request_count = 0
        # 定义set集合，用于存储指纹数据
        # 2.修改init方法，创建去重容器
        self.filter_container = FilterContainer()

        # 定义变量，用于统计过滤掉多少请求
        # self.filter_request_count = 0
    def clear(self):
        """清除Redis中的指纹和请求数据"""
        if settings.SCHEDULE_PERSIST:
            # 清空redis队列中的数据
            self.queue.clear()
            # 清空指纹数据
            self.filter_container.clear()

    def add_request(self, request):
        # 3.2.1-4:使用stats_collector来统计总入对请求数量和过滤掉的请求数量
        # 3.3.1-2:只有需要过滤．并且重复了，才需要过滤
        if not request.dont_filter and self.seen_request(request):
            # 如果重复，就记录日志
            logger.info('过滤掉重复请求{}'.format(request.url))
            # self.filter_request_count += 1
            self.stats_collector.incr_filter_request_count()
            return

        # 添加请求对象
        self.queue.put(request)
        # print('endend..')
        # 2.0.2-5:每次添加请求的时候，就让total_request_count + 1
        # 此时的请求数量为入对的请求数量
        # self.total_request_count += 1
        self.stats_collector.incr_total_request_count()

    def get_request(self):
        # 获取请求对象
        return self.queue.get()

    def seen_request(self, request):
        # 用于爬虫请求是否已经被爬取过了
        # 获取请求获取请求对应的指纹
        fp = self._gen_fp(request)
        # 判断fp是否在容器中
        if self.filter_container.exists(fp):
            # 返回True,说明这个请求重复
            return True
        self.filter_container.add_fp(fp)
        # 返回False　说明这个请求不重复
        return False

    def _gen_fp(self, request):
        """
        根据请求对象生成指纹
        :param request: 请求对象
        :return: 请求对应的指纹
        思路:
            1.明确需要使用哪些数据生成指纹
                1.URL，方法名，params,data
            2.准备数据
            3.把数据添加到sha1算法中
            4.通过sha1获取16进制的指纹
        """
        # 2.准备数据
        # 对url进行规范化处理
        url = canonicalize_url(request.url)
        # 方法名
        method = request.method.upper()

        # GET的请求参数
        params = request.params if request.params else {}
        # 但是字典是无序的,我们把他转换成元祖再排序
        params = sorted(params.items(), key=lambda x: x[0])

        # POST请求的请求体数据
        data = request.data if request.data else {}
        # 但是字典是无序的,我们把他转换成元祖再排序
        data = sorted(data.items(), key=lambda x: x[0])

        # 获取sha1对象
        sha1 = hashlib.sha1()
        # 更新数据
        sha1.update(self.get_bytes_from_str(url))
        sha1.update(self.get_bytes_from_str(method))
        sha1.update(self.get_bytes_from_str(str(params)))
        sha1.update(self.get_bytes_from_str(str(data)))
        # 获取16进制的指纹数据
        return sha1.hexdigest()

    # py3中字符串默认是str,str就是一个unicode的字符串
    # py2中字符串str是二进制数据，解码后是unicode类型

    def get_bytes_from_str(self, s):
        if six.PY3:
            # 如果是py3，如果是字符串str就进行编码
            if isinstance(s, str):
                return s.encode('utf8')
            else:
                return s
        else:
            # py2,如果是str类型就直接返回,decode()之后变为unicode
            if isinstance(s, str):
                return s
            else:
                # 在py2中encode默认使用ascli码进行编码的，所以此处不能省
                return s.decode('utf8')
