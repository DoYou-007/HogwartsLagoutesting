import requests


class Base:
    def __init__(self):
        #获取token值
        corpsecret = "1THBiH5O2--rLUx0xrPzYVISdvvRdf8rTwJNN5KXgtc"
        corid = "wwf2413e18b7b6d39c"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corid}&corpsecret={corpsecret}"
        r = requests.get(url).json()
        self.access_token = r['access_token']

        #申明一个session
        self.s = requests.Session()

        #在session中添加token值
        self.s.params = {'access_token':self.access_token}

    def send(self,*args,**kwargs):
        r = self.s.request(*args,**kwargs)
        return r.json()
