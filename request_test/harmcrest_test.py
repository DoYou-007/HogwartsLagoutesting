# hamcrest断言练习
import requests
from hamcrest import *


def test_hamcrest():
    r = requests.get('https://ceshiren.com/categories.json')
    print(r.json()['category_list']['categories'][0]['name'])
    # assert r.json()['category_list']['categories'][0]['name'] == '开源项目'
    # assert  jsonpath(r.json(),'$..name')[0] == '开源项目'
    assert_that(r.json()['category_list']['categories'][0]['name'],equal_to('开源项目'))
test_hamcrest()