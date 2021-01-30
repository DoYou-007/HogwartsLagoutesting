import requests
import pytest

# r = requests.get("https://httpbin.testing-studio.com/get")
# print(r.status_code)  #获取响应的编码
# print(r.text)  #获取返回具体内容
# print(r.json())   #返回内容以json的格式展示

#简短的测试用例
class TestDemo():
    def testdemo(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert  r.status_code ==200

#接口请求构造get/post/put/head：get query 请求

    def test_query(self):
        playload = {
            'level':1,
            'name':"seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get",params=playload)
        print(r.text)
        assert r.status_code == 200

#接口请求构造get/post/put/head：form 请求参数构造

    def test_post(self):
        payload = {'key1':1,'key2':2}
        r = requests.post("https://httpbin.org/post",data=payload)
        print(r.text)
        assert r.status_code == 200


# 接口请求构造get/post/put/head：head的构造



# if __name__ == "__main__":
#     pytest.main('-v -s')

R = TestDemo()
# R.testdemo()
# R.test_query()
R.test_post()