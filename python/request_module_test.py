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
# i = Image.open(BytesIO(c.content))

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

   #但一般情况下，你应该使用下面的模式将文本流保存到文件
# r = requests.get("http://httpbin.org/events",stream=True)
# with open('req_test.txt','wb') as fd :
#     for chunk in r.iter_content(chunk_size=4):
#         fd.write(chunk)

""" 定制请求头 """
url = 'https://api.github.com/some/endpoint'
headers = {'user-agent':'my-app/0.01'}
r1 = requests.get(url,headers=headers)
r2 = requests.get(url)
print(r1)
print(r2)