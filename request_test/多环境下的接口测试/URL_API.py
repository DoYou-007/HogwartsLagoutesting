import base64
import json

import requests
import yaml

class API:
    # #将请求的不同环境的接口写成配置类文件，支持进行切换
    # evn = {
    #     'dev':'0.0.0.0:9998',
    #     'test':'0.0.0.0:9999'
    # }

    # # 对请求配置文件进一步进行优化，让测试环境直接从配置中修改
    # evn = {
    #     'default':'test',
    #     'stage':{
    #         'dev': '0.0.0.0:9998',
    #         'test': '0.0.0.0:9999'
    #     }
    # }

    evn = yaml.safe_load(open('evn.yaml'))
    print(evn)

    #对请求接口进行二次封装，实现请求进行定制化
    def send(self,data:dict):

        #对请求接口做处理，支持替换成测试接口
        URL = str(data['url']).replace('test_home',self.evn['stage'][self.evn['default']])

        r = requests.request(method= data['method'],url= URL,headers= data['headers'])
        return r

    def decode_data(self,data:dict):
        if data['encoding'] == 'base64':
            self.send(data)
            return json.loads(base64.b64decode(self.send(data).content))
        elif data['encoding'] == 'private':
            return  requests.request('url',data = self.send(data).content)
