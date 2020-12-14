import requests

# r = requests.get("https://httpbin.testing-studio.com/get")
# print(r.status_code)  #获取响应的编码
# print(r.text)  #获取返回具体内容
# print(r.json())   #返回内容以json的格式展示

#简短的测试用例
class TestDemo:
    def testdemo(self):
        r = requests.get("https://httpbin.testing-studio.com/get")
        print(r.status_code)
        print(r.text)
        print(r.json())
        assert  r.status_code ==200


# R = TestDemo()
# R.testdemo()

#接口请求构造get/post/put/head：get query 请求

    def test_query(self):
        playload = {
            'level':1,
            'name':"seveniruby"
        }
        r = requests.get("https://httpbin.testing-studio.com/get",params=playload)
        print(r.text)
        assert r.status_code == 200