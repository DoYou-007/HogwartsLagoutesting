# from mitmproxy import ctx
#
# #mitmproxy插件的简单实例
# class Counter:
#     def __init__(self):
#         self.num = 0
#
#     def request(self, flow):
#         self.num = self.num + 1
#         ctx.log.info("hello")
#         ctx.log.info("We've seen %d flows" % self.num)
# #将定义的类放到addons事件中，mitmproxy才能够识别
# addons = [
#     Counter()
# ]


#如下是将百度网址定向为hello world 的简单实例
# from mitmproxy import http
#
# class Counter:
#     def __int__(self):
#         self.num = 0
#
#     def request(self,flow:http.HTTPFlow) -> None:
#
#         if "baidu" in flow.request.pretty_url:
#             flow.response = http.HTTPResponse.make(
#                 200,  # (optional) status code
#                 b"Hello World",  # (optional) content
#                 {"Content-Type": "text/html"}  # (optional) headers
#              )
#
# addons = [
#     Counter()
# ]


#对雪球app通过mitmproxy的方式进行代理实现修改股价：
from mitmproxy import http

class XueQiu:
    def __int__(self):
        self.num = 0

    def request(self,flow:http.HTTPFlow) -> None:

        if "v5/stock/batch/quote.json" in flow.request.pretty_url:
            with open (r"/Users/xieguojun/Hogwarts/HogWarts/HogwartsLagoutesting/http/quote.json",'r',encoding='utf-8') as f:
                flow.response = http.HTTPResponse.make(
                    200,  # (optional) status code
                    f.read(),  # (optional) content
                    {"Content-Type": "application/json"}  # (optional) headers
                 )

addons = [
    XueQiu()
]