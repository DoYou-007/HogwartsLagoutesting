from unittest import TestCase
from 基于加密接口的测试用例设计.defrent_apirequest import ApiRequest

class TestApiRequest(TestCase):
    #提供模拟数据
    re_data ={
        'method':"get",
        'url':'http://0.0.0.0:9999/demo1.txt',
        'headers':None,
        'encoding':'base64'
    }

    #进行封装方法的测试
    def test_send(self):
        re = ApiRequest()
        print(re.send(self.re_data))
