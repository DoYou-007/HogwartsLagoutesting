import  requests

def test_qiyeweixin():

    #get_access_token
    corpsecret = "1THBiH5O2--rLUx0xrPzYVISdvvRdf8rTwJNN5KXgtc"
    corid = "wwf2413e18b7b6d39c"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corid}&corpsecret={corpsecret}"

    r= requests.get(url)
    access_token = r.json()['access_token']
    # print(access_token)


    #获取成员信息
    userid = "XieGuoJun"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid={userid}"
    r = requests.get(url)
    # print(r.json())

    #更新成员
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update?access_token={access_token}"
    data = {
        "userid": "HeQi",
        "name": "阿丽"
    }
    r = requests.post(url=url,json=data)
    # print(r.json())

    #添加成员：
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
    data = {
        "userid": "xiaolai",
        "name": "小赖",
        "mobile": "13800000900",
        "department": [1]
    }
    r = requests.post(url,json=data)
    print(r.json())

    #删除成员：
    # userid = "xiaolai"
    # url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={access_token}&userid={userid}"
    # r = requests.get(url)
    # print(r.json())
