# coding:utf8
"""
下载器中间件：
1.用于处理请求和响应
2.4-1:定义一个中间件文件夹．里面又downloader_middleware.spider_middleware
"""


class BaiduDownloaderMiddleware(object):
    def process_request(self,request):
        print('BaiduDownloaderMiddleware:process_request')
        return request

    def process_response(self,response):
        #　处理请求
        print('BaiduDownloaderMiddleware:process_response')

        return response

class DoubanDownloaderMiddleware(object):
    def process_request(self,request):
        print('DoubanDownloaderMiddleware:process_request')
        return request

    def process_response(self,response):
        #　处理请求
        print('DoubanDownloaderMiddleware:process_response')

        return response