# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/21 13:33
# @File     : python_yaml.py

import yaml

# print(yaml.load("""
#     - hellp
#     - nihao
#     - nchdkl
#     - nihaok
# """,Loader=yaml.FullLoader)) #显示的更加简介防止报错
#
# print(yaml.load("""
#     a: 1
# """,Loader=yaml.FullLoader)) #显示的更加简介防止报错
#
# print(yaml.load(open('demo.yaml'),Loader=yaml.FullLoader))  #读取yaml文件内容
#
# print(yaml.dump({'a': [1, 2]}))
#
# with open('demo2.yaml','w') as f:
#     yaml.dump(data={'a':[2,3]},stream=f)

print(yaml.dump({"extract": [
    {"token": "content.token"}
]}))

print(yaml.load("""
        extract:
            hash: 'content.hash'
        """, Loader=yaml.FullLoader))
