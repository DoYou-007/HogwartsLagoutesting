import json

import requests

# r = requests.get('http://api.github.com/events')
# print(r)
# b = r = requests.post('http://httpbin.org/post',data = {'key':'value'})
# print(b.text)
# print(b.cookies)
#
# print('- '*100)
# payload = {'key1': 'value1', 'key2': 'value2'}
# d = requests.get("http://httpbin.org/get",params=payload)
# print(d.url)
# print(d.text)
#
# print('- '*100)
# payload = {'key1': 'value1', 'key2':  ['value2', 'value3']}
# c = requests.get("http://httpbin.org/get",params=payload)
# print(c.url)
# e = c.headers
# print(e['Content-Type'])
# f = {'Date': 'Thu, 16 Jul 2020 14:37:28 GMT', 'Content-Type': 'application/json', 'Content-Length': '421', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
# print(f['Date'])


"""
Requests 会自动为你解码 gzip 和 deflate 传输编码的响应数据。
例如，以请求返回的二进制数据创建一张图片，你可以使用如下代码：
参考资料：https://requests.readthedocs.io/zh_CN/latest/user/quickstart.html
"""
# from PIL import Image
# from io import BytesIO
# r = requests.get('https://api.github.com/events')
# i = Image.open(BytesIO(r.content))

"""json响应格式："""
# print('- '*100)
# # r = requests.get('http://www.baidu.com')   #返回的是一个页面
# # r = requests.get('https://api.github.com/events')  接口响应超时
# r = requests.get("http://httpbin.org/get",params=payload)
# print(r.json())
# print(r.status_code)

"""原始响应内容："""
# print('- '*100)
# r = requests.get("http://httpbin.org/events",stream=True)
# print(r.raw)
# print(r.raw.read().decode('utf-8'))

# 但一般情况下，你应该使用下面的模式将文本流保存到文件
# r = requests.get("http://httpbin.org/events",stream=True)
# with open('req_test.txt','wb') as fd :
#     for chunk in r.iter_content(chunk_size=4):
#         fd.write(chunk)

""" 二进制响应内容 """
# r = requests.get('https://api.github.com/events')
# print(r.text)
# print(r.content)


""" 定制请求头 """
# url = 'https://api.github.com/some/endpoint'
# headers = {'user-agent':'my-app/0.01'}
# r1 = requests.get(url,headers=headers)
# r2 = requests.get(url)
# print(r1)
# print(r2)

# 接口模拟请求浏览器配置接口
# https://api.browser.miui.com/bsr/pref?append=eyJsYW5ndWFnZSI6InpoLXJDTiIsInJlZ2lvbiI6IkNOIiwiZGV2aWNlIjoibGFuY2Vsb3QiLCJtb2RlbCI6Ik0yMDA0SjE5QyIsInByb2R1Y3QiOiJsYW5jZWxvdCIsInZlcnNpb25fcmVsZWFzZSI6IjEwIiwidmVyc2lvbl9pbmNyZW1lbnRhbCI6IjIwLjUuMTEiLCJtaXVpX3ZlcnNpb25fbmFtZSI6IlYxMiIsInZlcnNpb25fbmFtZSI6IjEyLjYuMCIsInZlcnNpb25fY29kZSI6MTIwNjAwMDAwLCJwYWNrYWdlX25hbWUiOiJjb20uYW5kcm9pZC5icm93c2VyIiwiaXNUYWJsZXQiOmZhbHNlLCJwbGF0Zm9ybSI6IkFSTSIsInN0YWJsZSI6ImRldiIsInNjcmVlbl93aWR0aCI6IjEwODAiLCJzY3JlZW5faGVpZ2h0IjoiMjEzNCIsInNjcmVlbl9kZW5zaXR5IjoiNDQwIiwiY2FycmllciI6InVua25vd24iLCJvcGVyYXRvciI6InVua25vd24iLCJkZXZpY2VfaGFzaCI6ImM2Nzg3M2M4YWRlYWQ0ZTQ3ZTNiMWYyOWRhYzM1OWQxIiwiZGV2aWNlX2lkIjoiMmMzMDE2ODA1ZTVmOTNjMGUwYWY2ZWJhODE3ZmRhMmMiLCJkZXZpY2VfaWRfbGlzdCI6IlsyYzMwMTY4MDVlNWY5M2MwZTBhZjZlYmE4MTdmZGEyYywgYzY3ODczYzhhZGVhZDRlNDdlM2IxZjI5ZGFjMzU5ZDFdIiwibW9iaWxlX2lkX2xpc3QiOiJbMzg0ODEzNTNmOGE4OTIwNTkzMzAwYTZjNGZkYTUxY2VdIiwiYW5kcm9pZF9pZCI6IjJhYTQwODE3YzFhZDc4ZmUiLCJ1ZGlkIjoiIiwib2FpZCI6IjMyYWM4MjQ2ZjZlMTBlYjIiLCJ2YWlkIjoiOGI5MzhkNzA5NGNjMzZmZiIsImltZWkiOiJjNjc4NzNjOGFkZWFkNGU0N2UzYjFmMjlkYWMzNTlkMSIsImltZWkxIjoiMmMzMDE2ODA1ZTVmOTNjMGUwYWY2ZWJhODE3ZmRhMmMiLCJpbWVpMiI6ImM2Nzg3M2M4YWRlYWQ0ZTQ3ZTNiMWYyOWRhYzM1OWQxIiwibnQiOiJ3aWZpIiwic250IjoiIiwiaW5Qcml2YXRlIjoiMCIsImlzU2ltcGxlSG9tZSI6IjAiLCJjbWNjX2RldmljZSI6ImZhbHNlIiwicmVzdHJpY3RJbWVpIjoiZmFsc2UifQ==&key=5bf52342144d12a30585c895056e66c0&client_version_code=120600000&client_version_name=12.6.0&isAdvertisingEnabled=true&miuiStable=2
# datas = {
#     "append":"eyJsYW5ndWFnZSI6InpoLXJDTiIsInJlZ2lvbiI6IkNOIiwiZGV2aWNlIjoibGFuY2Vsb3QiLCJtb2RlbCI6Ik0yMDA0SjE5QyIsInByb2R1Y3QiOiJsYW5jZWxvdCIsInZlcnNpb25fcmVsZWFzZSI6IjEwIiwidmVyc2lvbl9pbmNyZW1lbnRhbCI6IjIwLjUuMTEiLCJtaXVpX3ZlcnNpb25fbmFtZSI6IlYxMiIsInZlcnNpb25fbmFtZSI6IjEyLjYuMCIsInZlcnNpb25fY29kZSI6MTIwNjAwMDAwLCJwYWNrYWdlX25hbWUiOiJjb20uYW5kcm9pZC5icm93c2VyIiwiaXNUYWJsZXQiOmZhbHNlLCJwbGF0Zm9ybSI6IkFSTSIsInN0YWJsZSI6ImRldiIsInNjcmVlbl93aWR0aCI6IjEwODAiLCJzY3JlZW5faGVpZ2h0IjoiMjEzNCIsInNjcmVlbl9kZW5zaXR5IjoiNDQwIiwiY2FycmllciI6InVua25vd24iLCJvcGVyYXRvciI6InVua25vd24iLCJkZXZpY2VfaGFzaCI6ImM2Nzg3M2M4YWRlYWQ0ZTQ3ZTNiMWYyOWRhYzM1OWQxIiwiZGV2aWNlX2lkIjoiMmMzMDE2ODA1ZTVmOTNjMGUwYWY2ZWJhODE3ZmRhMmMiLCJkZXZpY2VfaWRfbGlzdCI6IlsyYzMwMTY4MDVlNWY5M2MwZTBhZjZlYmE4MTdmZGEyYywgYzY3ODczYzhhZGVhZDRlNDdlM2IxZjI5ZGFjMzU5ZDFdIiwibW9iaWxlX2lkX2xpc3QiOiJbMzg0ODEzNTNmOGE4OTIwNTkzMzAwYTZjNGZkYTUxY2VdIiwiYW5kcm9pZF9pZCI6IjJhYTQwODE3YzFhZDc4ZmUiLCJ1ZGlkIjoiIiwib2FpZCI6IjMyYWM4MjQ2ZjZlMTBlYjIiLCJ2YWlkIjoiOGI5MzhkNzA5NGNjMzZmZiIsImltZWkiOiJjNjc4NzNjOGFkZWFkNGU0N2UzYjFmMjlkYWMzNTlkMSIsImltZWkxIjoiMmMzMDE2ODA1ZTVmOTNjMGUwYWY2ZWJhODE3ZmRhMmMiLCJpbWVpMiI6ImM2Nzg3M2M4YWRlYWQ0ZTQ3ZTNiMWYyOWRhYzM1OWQxIiwibnQiOiJ3aWZpIiwic250IjoiIiwiaW5Qcml2YXRlIjoiMCIsImlzU2ltcGxlSG9tZSI6IjAiLCJjbWNjX2RldmljZSI6ImZhbHNlIiwicmVzdHJpY3RJbWVpIjoiZmFsc2UifQ==",
#     'key':"5bf52342144d12a30585c895056e66c0",
# }
# url = "https://api.browser.miui.com/bsr/pref"
# r = requests.get(url,params=datas)
# # print(r.json())
# print(r.text)
# print(r.url)

""" 更加复杂的Post请求 
通常，你想要发送一些编码为表单形式的数据——非常像一个 HTML 表单。要实现这个，只需简单地传递一个字典给 data 参数
"""
# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.post('http://httpbin.org/post',data=payload)
# print(r.text)

# 元组的形式
# print('* '*100)
# payload1 = (('key1','value1'),('key2','value2'))
# r = requests.post('http://httpbin.org/post',data=payload1)
# print(r.text)

# 很多时候你想要发送的数据并非编码为表单形式的。如果你传递一个 string 而不是一个 dict，那么数据会被直接发布出去。
# 例如，Github API v3 接受编码为 JSON 的 POST/PATCH 数据   运行的时候存在问题提示not found
url = 'http://httpbin.org/post'
payload3 = {'some': 'data'}
r = requests.post(url, data=json.dumps(payload3))
# r = requests.post(url,json=payload3)     #json参数直接进行编码
print(r.text)

"""  """
