#封装解密方法，方便调用
import base64
import json

import requests

class ApiRequest():
    def send(self,data:dict):
        res = requests.request(data['method'],data['url'],headers = data['headers'])
        if data['encoding'] == 'base64':
            return json.loads(base64.b64decode(res.content))

        #使用的是第三方的加密接口时，直接进行访问对方的解密接口，得到解密后的信息
        elif data['encoding'] == 'private':
            return requests.post('url',data=res.content)