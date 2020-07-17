# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/16 17:54
# @File     : urllib_moudle.py

import urllib.request
from urllib import request, parse
import json

# response:object = urllib.request.urlopen("https://www.baidu.com")
# print(response.status)
# rep = response.read()
# print(rep.decode('utf-8'))
# print("------------------")
# print(type(rep))
# rep2 = rep.decode('ascii')
# print(rep2)
# print(type(rep2))

"""
urllib的request模块可以非常方便地抓取URL内容，也就是发送一个GET请求到指定的页面，然后返回HTTP的响应：
例如，对豆瓣的一个URLhttps://api.douban.com/v2/book/2129650进行抓取，并返回响应：
"""
# with request.urlopen("https://www.baidu.com") as f:
#     data = f.read()
#     print('Status:',f.status,f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('data:',data.decode('utf-8'))

"""
如果我们要想模拟浏览器发送GET请求，就需要使用Request对象，通过往Request对象添加HTTP头，我们就可以把请求伪装成浏览器。例如，模拟iPhone 6去请求豆瓣首页：
"""
# print('- '*100)
# req = request.Request("http://www.douban.com/")
# req.add_header('User-Agent','Mozilla/5.0 (Linux; U; Android 10; zh-cn; M2004J19C Build/QP1A.190711.020) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/71.0.3578.141 Mobile Safari/537.36 XiaoMi/MiuiBrowser/12.6.0')
# with request.urlopen(req) as f:
#     print('Status:',f.status,f.reason)
#     for k, v in f.getheaders():
#         print('%s:%s'%(k,v))
#     print('data:',f.read().decode('utf-8'))

"""
发送post请求：需要将参数data以bytes形式传入
我们模拟一个微博登录，先读取登录的邮箱和口令，然后按照weibo.cn的登录页的格式以username=xxx&password=xxx的编码传入：
"""
print('login to weibo.com')
email = input('Email:')
passwd = input('Password')
login_data = parse.urlencode([
    ('username', email),
    ('password', passwd),
    ('entry', 'mweibo'),
    ('client_id', ''),
    ('savestate', '1'),
    ('ec', ''),
    ('pagerefer', 'https://passport.weibo.cn/signin/welcome?entry=mweibo&r=http%3A%2F%2Fm.weibo.cn%2F')
])

req = request.Request('https://passport.weibo.cn/sso/login')
req.add_header('Origin', 'https://passport.weibo.cn')
req.add_header('User-Agent',
               'Mozilla/6.0 (iPhone; CPU iPhone OS 8_0 like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko) Version/8.0 Mobile/10A5376e Safari/8536.25')
req.add_header('Referer',
               'https://passport.weibo.cn/signin/login?entry=mweibo&res=wel&wm=3349&r=http%3A%2F%2Fm.weibo.cn%2F')

with request.urlopen(req, data=login_data.encode('utf-8')) as f:
    print('status', f.status, f.reason)
    for k, v in f.getheaders():
        print('%s: %s' % (k, v))
    print('Data:', f.read().decode('utf-8'))
