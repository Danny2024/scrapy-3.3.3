# coding:utf8
"""
下载器中间件：
1.用于处理请求和响应
"""


class DownloaderMiddleware(object):
    def process_request(self,request):
        print('DownloaderMiddleware:process_request')
        return request

    def process_response(self,response):
        #　处理请求
        print('DownloaderMiddleware:process_response')

        return response