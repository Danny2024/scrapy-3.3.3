# coding:utf8
"""
下载器模块
1.根据请求对象，发送请求，获取相应数据，封装为Reponse对象返回

"""
import requests
from ..http.response import Response


class DownLoader(object):
    def get_response(self, request):
        if request.method.upper() == "GET":
            res = requests.get(request.url,headers=request.headers,params=request.params,cookies=request.cookies)
        elif request.method.upper() == "POST":
            res = requests.post(request.url,headers=request.headers, cookies=request.cookies)
        else:
            raise Exception('暂时只支持GET和POST请求')

        return Response(res.url,res.status_code,res.headers, res.content)





