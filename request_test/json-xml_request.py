import requests as requests
from requests_xml import XMLSession
from jsonpath import jsonpath


# json请求体构造
def test_json_post():
    pageload = {
        'level':1,
        'name':'xieguojun'
    }
    r = requests.post('http://httpbin.org/post',json=pageload)
    assert r.status_code == 200
    assert r.json()['json']['level'] == 1

test_json_post()


#xml请求体构造：
# def test_post_xml():
    # xml: Union[bool, Any] = ''''''<?xml version='1.0' encoding='utf-8'?> <a>&</a>''''''
    # headers = {'Content-Type':'application/xml'}
    # r = requests.post('http://httpbin.org/post',data=xml,headers = headers )
    # print(r.text)


#json格式断言：
def test_hogwarts_json():
    r = requests.get('https://ceshiren.com/categories.json')
    print(r.json()['category_list']['categories'][0]['name'])
    assert r.json()['category_list']['categories'][0]['name'] == '开源项目'

test_hogwarts_json()

# json_path断言：
def test_hogwarts_json():
    r = requests.get('https://ceshiren.com/categories.json')
    print(r.json()['category_list']['categories'][0]['name'])
    # assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
    assert  jsonpath(r.json(),'$..name')[0] == '开源项目'

test_hogwarts_json()

# xml断言、xpath断言、xml解析
def test_xml_assertion():
    session = XMLSession()
    # 发起请求
    r = session.get('https://www.nasa.gov/rss/dyn/lg_image_of_the_day.rss')
    # 获取接口的链接
    print(r.xml.links)
    #通过xpath进行断言
    item = r.xml.xpath('//item',first=True)
    print(item.text)

test_xml_assertion()