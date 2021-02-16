import  requests


class Test_Header:

    # 练习如何在header中带上cookie信息
    def test_add_headercookie(self):
        header = {'Cookies':'hello_cookies'}
        r = requests.get('https://httpbin.testing-studio.com/cookies',headers=header)
        print(r.request.headers)

    #自定义header的信息内容
    def test_add_selfheader(self):
        header1 = {
            'Cookies': 'hello_cookies',
            'User-Agent':'add_self_user-agenet'
        }
        r = requests.get('https://httpbin.testing-studio.com/cookies', headers=header1)
        print(r.request.headers)

    #使用cookie参数继续传输cookie信息，也可支持传输多个内容
    def test_use_cookies(self):
        header = {'User-Agent':'add_self_user-agenet'}
        # cookie = {
        #     'something':'youself_cookie' ,
        #     'name':'xiexie'
        # }
        #第二种书写方式
        cookie = dict(something='youself_cookie',name='xiexie')
        r = requests.get('https://httpbin.testing-studio.com/cookies', headers=header,cookies= cookie)
        print(r.request.headers)

