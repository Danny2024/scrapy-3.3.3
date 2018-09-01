# 去重容器
# scrapy_plus/utils/set.py
import redis
from scrapy_plus.conf import settings


class BaseFilterContainer(object):

    def add_fp(self, fp):
        '''往去重容器添加一个指纹'''
        pass

    def exists(self, fp):
        '''判断指纹是否在去重容器中'''
        pass

class NoramlFilterContainer(BaseFilterContainer):
    def __init__(self):
        """内存版----去重容器，使用set集合存储指纹数据"""
        # 一个下划线是受保护的.不能通过from xxx import * 进行导入
        # 两个下划线是私有，只能本类中使用，外边不能用
        # __xxx__内置的魔法方法，只能本类中使用，外边不能用
        self._filter_container = set()

    def add_fp(self, fp):
        # 添加指纹到set集合中
        self._filter_container.add(fp)

    def exists(self, fp):
        if fp in self._filter_container:
            return True
        else:
            return False

from ..conf.settings import REDIS_SET_NAME,REDIS_HOST,REDIS_PORT,REDIS_DB
import redis

class RedisFilterContainer(BaseFilterContainer):
    '''利用redis的指纹集合,redis版----去重容器'''

    def __init__(self, name=REDIS_SET_NAME, host=REDIS_HOST, port=REDIS_PORT, db=REDIS_DB):
        # 建立redis数据库链接
        self.__server = redis.StrictRedis(host=host,port=port,db=db)
        # set集合在redis中的key
        self.name = name
    def add_fp(self,fp):
        """把指纹添加到redis的set集合中"""
        self.__server.sadd(self.name,fp)
    def exists(self, fp):
        """判断是否存储"""
        return self.__server.sismember(self.name,fp)
    def clear(self):
        """清空指纹数据"""
        self.__server.delete(self.name)


