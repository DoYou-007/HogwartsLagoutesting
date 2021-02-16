import requests
from requests.auth import HTTPBasicAuth

#Http  basic的定义：基本认证，是允许http用户代理在请求时，提供用户名和秘密的一种方式

def test_oauth():
    r = requests.get('https://httpbin.testing-studio.com/basic-auth/xie/12345',auth= HTTPBasicAuth('xie','12345'))
    print(r.text)
    print(r.status_code)