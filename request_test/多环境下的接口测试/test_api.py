#对二次封装接口进行测试
import yaml
import base64
import json


from 多环境下的接口测试 import URL_API
from 基于加密接口的测试用例设计.defrent_apirequest import  ApiRequest

class TestAPI:
    data = {
        'method': 'get',
        'url': 'http://test_home/demo1.txt',
        'headers': None,
        'encoding':'private'
    }

    def test_send(self):
        api = URL_API.API()
        # print(api.send(self.data).text)
        data = api.send(self.data).content
        print(json.loads(base64.b64decode(data)))

    #校验yaml文档
    def test_get_yaml(self):
        evn = yaml.safe_load(open('evn.yaml'))
        print(evn)

    def test_encode_data(self):
        api = URL_API.API()
        print(api.decode_data(self.data))