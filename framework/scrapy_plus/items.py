# coding:utf8
"""
封装爬虫提取出来的数据
- 将来可以根据这个类型来判断爬虫提取的是数据还是请求
"""

class Item(object):
    def __init__(self,data):
        # 这是为私有属性，为了保护Item中封装的数据
        self.__data = data

    # 只能获取值，不能赋值
    @property
    def data(self):
        return self.__data