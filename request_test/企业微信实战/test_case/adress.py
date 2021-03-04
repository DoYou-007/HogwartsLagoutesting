import requests
from test_case.base import Base


class Adress(Base):

    def  add_member(self,userid:str,name:str,mobile:int,department:list,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/create"
        data = {
            "userid": userid,
            "name": name,
            "mobile": mobile,
            "department": department
        }
        data.update(kwargs)
        return self.send('post',url, json=data)


    def get_member(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?userid={userid}"
        return self.send('get',url)


    def delete_member(self,userid):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?userid={userid}"
        return self.send('get',url)

    def update_member(self,userid,name,**kwargs):
        url = f"https://qyapi.weixin.qq.com/cgi-bin/user/update"
        data = {
            "userid": userid,
            "name": name
        }
        data.update(kwargs)
        return self.send('post',url=url, json=data)