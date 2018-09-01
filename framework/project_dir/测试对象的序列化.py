import pickle

from scrapy_plus.http.request import Request

# 创建request对象
request = Request('http://www.baidu.com')

# 序列化 对象-->二进制
data = pickle.dumps(request)
print(data)
# 反序列化
req = pickle.loads(data)
print(req.url)
print(req)
