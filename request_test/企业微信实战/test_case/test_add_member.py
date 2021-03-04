import requests


def test_add_member():
    # get_access_token
    corpsecret = "1THBiH5O2--rLUx0xrPzYVISdvvRdf8rTwJNN5KXgtc"
    corid = "wwf2413e18b7b6d39c"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corid}&corpsecret={corpsecret}"

    r = requests.get(url)
    access_token = r.json()['access_token']
    # print(access_token)

    # 清空操作：
    userid = "studay123"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={access_token}&userid={userid}"
    r = requests.get(url)
    print(r.json())

    # 添加成员：
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={access_token}"
    data = {
        "userid": "studay123",
        "name": "菜比",
        "mobile": "13800000911",
        "department": [1]
    }
    r = requests.post(url, json=data)
    print(r.json())

    #查询是否添加成功
    userid = "studay123"
    url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={access_token}&userid={userid}"
    r = requests.get(url)
    print(r.json())
