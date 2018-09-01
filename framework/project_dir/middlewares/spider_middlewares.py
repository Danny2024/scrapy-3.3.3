# coding:utf8
"""
爬虫中间件
"""


class BaiduSpiderMiddleware(object):
    def process_request(self, request):
        print('BaiduSpiderMiddleware:process_request')
        return request

    def process_response(self, response):
        # 　处理请求
        print('BaiduSpiderMiddleware:process_response')

        return response


class DoubanSpiderMiddleware(object):
    def process_request(self, request):
        print('DoubanSpiderMiddleware: process_request')
        return request

    def process_response(self, response):
        # 　处理请求
        print('DoubanSpiderMiddleware:process_response')

        return response


