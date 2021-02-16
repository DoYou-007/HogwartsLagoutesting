#对于返回数据进行了加密的内容进行解密处理
import base64
import json

import requests

def test_encryption():
    r =requests.get('http://0.0.0.0:9999/demo1.txt')
    print(r.text)
    rec = json.loads(base64.b64decode(r.text))
    print(rec)