# coding:utf8
"""
爬虫中间件
"""


class SpiderMiddleware(object):
    def process_request(self, request):
        print('SpiderMiddleware:process_request')
        return request

    def process_response(self, response):
        # 　处理请求
        print('SpiderMiddleware:process_response')

        return response


