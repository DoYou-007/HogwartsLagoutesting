import time

import requests


# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'en-US,en;q=0.9',
#     'Connection': 'keep-alive',
#     'Host': '1463506423.ax.nofollow.51wtp.com',
#     'Referer': 'http://1463506423.ax.nofollow.51wtp.com/index.php/toupiao/h5/detail?id=3201248&vid=104m493p5yq9dn8&__cf_chl_jschl_tk__=f7c31d52f4efe6d0f7ae54688ebb0a301a0ad969-1611750213-0-ARYCRYwJEK8vw_XZ-yB72UfpD5YPUh2UyCCWH1qSJk6wWnM4ixgzbJuqBZ9mGht1t6xrv72MP5zxLH333qvAHrASngq-_P4Jz1hqjesdx4Moi2hEt-0vtV1HMEY3tCGkIegPe4ypwqeYbnoK-NtWrCpDAcyjpgh0Yor8sxgVPY1E5fFI2fTiW8FHQtho1PjOloaZYLRGCACGC59l74u7zBaxOi95ne9HUmPyBykL7-iLyXPBJmgcUtBiacWbic6D-Sc8Iy7McVXgRzVnmGAGhMJxb1SLffX_XpaK8lnhdNMNb6OrLuNiYuYMnwZBk-UmL_3YRwUE1gZ3XurnIXFmV7Wbp_rhdNUpaankvWFXvx8RvOgf4J874HhsxjFh_uyYRw',
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.9 Safari/537.36',
#     'Upgrade-Insecure-Requests': '1',
#     'Cache-Control': 'max-age=0',
#     'Cookie':'cf_clearance=28d491258e48c59653730bd62739c48e003d271d-1611750217-0-150; __cfduid=d18cfd9978abacecd18b3788c0be156fe1611750217; PHPSESSID=q9b1ke62ipobbosfg4d9nd0164; __yjs_duid=1_a0799e6b96a22e9a782b0e2cedc775021611755313546; yjs_js_security_passport=a53ba6fe99a028cade130a2ff4901e869aeee7ec_1611755316_js'
# }
#
# url = 'http://1463506423.ax.nofollow.51wtp.com/index.php/toupiao/h5/detail?id=3201248&vid=104m493p5yq9dn8&__cf_chl_jschl_tk__=f7c31d52f4efe6d0f7ae54688ebb0a301a0ad969-1611750213-0-ARYCRYwJEK8vw_XZ-yB72UfpD5YPUh2UyCCWH1qSJk6wWnM4ixgzbJuqBZ9mGht1t6xrv72MP5zxLH333qvAHrASngq-_P4Jz1hqjesdx4Moi2hEt-0vtV1HMEY3tCGkIegPe4ypwqeYbnoK-NtWrCpDAcyjpgh0Yor8sxgVPY1E5fFI2fTiW8FHQtho1PjOloaZYLRGCACGC59l74u7zBaxOi95ne9HUmPyBykL7-iLyXPBJmgcUtBiacWbic6D-Sc8Iy7McVXgRzVnmGAGhMJxb1SLffX_XpaK8lnhdNMNb6OrLuNiYuYMnwZBk-UmL_3YRwUE1gZ3XurnIXFmV7Wbp_rhdNUpaankvWFXvx8RvOgf4J874HhsxjFh_uyYRw'
# param = {
#     'id': 3201248,
#     'vid': '104m493p5yq9dn8',
#     '__cf_chl_jschl_tk__': 'f7c31d52f4efe6d0f7ae54688ebb0a301a0ad969-1611750213-0-ARYCRYwJEK8vw_XZ-yB72UfpD5YPUh2UyCCWH1qSJk6wWnM4ixgzbJuqBZ9mGht1t6xrv72MP5zxLH333qvAHrASngq-_P4Jz1hqjesdx4Moi2hEt-0vtV1HMEY3tCGkIegPe4ypwqeYbnoK-NtWrCpDAcyjpgh0Yor8sxgVPY1E5fFI2fTiW8FHQtho1PjOloaZYLRGCACGC59l74u7zBaxOi95ne9HUmPyBykL7-iLyXPBJmgcUtBiacWbic6D-Sc8Iy7McVXgRzVnmGAGhMJxb1SLffX_XpaK8lnhdNMNb6OrLuNiYuYMnwZBk-UmL_3YRwUE1gZ3XurnIXFmV7Wbp_rhdNUpaankvWFXvx8RvOgf4J874HhsxjFh_uyYRw'
# }
#
# r = requests.get(url=url,data=param,headers=headers)
# print(r.text)



# """
# Accept: application/json, text/javascript, */*; q=0.01
# Accept-Encoding: gzip, deflate
# Accept-Language: en-US,en;q=0.9
# Connection: keep-alive
# Content-Length: 46
# Content-Type: application/x-www-form-urlencoded; charset=UTF-8
# Cookie: cf_clearance=28d491258e48c59653730bd62739c48e003d271d-1611750217-0-150; __cfduid=d18cfd9978abacecd18b3788c0be156fe1611750217; PHPSESSID=q9b1ke62ipobbosfg4d9nd0164; __yjs_duid=1_a0799e6b96a22e9a782b0e2cedc775021611755313546; yjs_js_security_passport=a53ba6fe99a028cade130a2ff4901e869aeee7ec_1611755316_js
# Host: 1463506423.ax.nofollow.51wtp.com
# Origin: http://1463506423.ax.nofollow.51wtp.com
# Referer: http://1463506423.ax.nofollow.51wtp.com/index.php/toupiao/h5/detail?id=3201248&vid=104m493p5yq9dn8&__cf_chl_jschl_tk__=f7c31d52f4efe6d0f7ae54688ebb0a301a0ad969-1611750213-0-ARYCRYwJEK8vw_XZ-yB72UfpD5YPUh2UyCCWH1qSJk6wWnM4ixgzbJuqBZ9mGht1t6xrv72MP5zxLH333qvAHrASngq-_P4Jz1hqjesdx4Moi2hEt-0vtV1HMEY3tCGkIegPe4ypwqeYbnoK-NtWrCpDAcyjpgh0Yor8sxgVPY1E5fFI2fTiW8FHQtho1PjOloaZYLRGCACGC59l74u7zBaxOi95ne9HUmPyBykL7-iLyXPBJmgcUtBiacWbic6D-Sc8Iy7McVXgRzVnmGAGhMJxb1SLffX_XpaK8lnhdNMNb6OrLuNiYuYMnwZBk-UmL_3YRwUE1gZ3XurnIXFmV7Wbp_rhdNUpaankvWFXvx8RvOgf4J874HhsxjFh_uyYRw
# User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.9 Safari/537.36
# X-Requested-With: XMLHttpRequest
#
# id: aZkXyu2Xz9pg
# vid: 104m493p5yq9dn8
# token: 5946
# """
#
# headers = {
#     'Accept':'application/json, text/javascript, */*; q=0.01',
#     'Accept-Encoding':'gzip, deflate',
#     'Accept-Language':'en-US,en;q=0.9',
#     'Connection':'keep-alive',
#     'Content-Length':'46',
#     'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
#     'Host':'1463506423.ax.nofollow.51wtp.com',
#     'Origin':'http://1463506423.ax.nofollow.51wtp.com',
#     'Referer':'http://1463506423.ax.nofollow.51wtp.com/index.php/toupiao/h5/detail?id=3201248&vid=104m493p5yq9dn8&__cf_chl_jschl_tk__=f7c31d52f4efe6d0f7ae54688ebb0a301a0ad969-1611750213-0-ARYCRYwJEK8vw_XZ-yB72UfpD5YPUh2UyCCWH1qSJk6wWnM4ixgzbJuqBZ9mGht1t6xrv72MP5zxLH333qvAHrASngq-_P4Jz1hqjesdx4Moi2hEt-0vtV1HMEY3tCGkIegPe4ypwqeYbnoK-NtWrCpDAcyjpgh0Yor8sxgVPY1E5fFI2fTiW8FHQtho1PjOloaZYLRGCACGC59l74u7zBaxOi95ne9HUmPyBykL7-iLyXPBJmgcUtBiacWbic6D-Sc8Iy7McVXgRzVnmGAGhMJxb1SLffX_XpaK8lnhdNMNb6OrLuNiYuYMnwZBk-UmL_3YRwUE1gZ3XurnIXFmV7Wbp_rhdNUpaankvWFXvx8RvOgf4J874HhsxjFh_uyYRw',
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.9 Safari/537.36',
#     'X-Requested-With':'XMLHttpRequest'
#
# }
#
# url = ' http://1463506423.ax.nofollow.51wtp.com/index.php/toupiao/h5/vote'
# param = {
#     'id': 'aZkXyu2Xz9pg',
#     'vid': '104m493p5yq9dn8',
#     'token': 5946
# }
#
# ip_adress = ['121.233.226.232','182.34.20.223','175.43.58.36']
#
# for i in ip_adress:
#     proxies = {'http':i}
#     r= requests.post(url=url,data=param,headers=headers,proxies=proxies)
#     print(r.json())


print((*(2,3,4,5)[:2],9,*(2,3,4,5)[2:]))
a = (2,3,4,5)
b = [[7,2],[5,4],[2,6]]
c = ((1,2),(3,4),(5,6))
d = [1,2,3]
d.append(4)
print('append的值',d)
d.extend(a)
# print(d)
e = {'name':'ni','age':23,'gender':'nan'}
print(e.items())
# print(dict(b),dir(b))

f = lambda x:x[0]
ed = sorted(b,key=lambda x:x[0])
print(ed)

nu = set()
nu.update({'x','y','z'})
nu.remove('z')
print(nu)
nu.clear()
print(nu)

second = [1,2,5,2,3,4,5,'x',4,'x']
print(list(set(second)))

a = ['Hello, 我是David', 'OK, 好', '很高兴认识你']
a_len = [len(item) for item in a ]
a_len_gbk = [len(item.encode('gbk')) for item in a]
print(a_len,a_len_gbk)

a = 'xxh/ddd/dd/'
b = a.split('/',3)
print(b)


a = [[0.468,0.975,0.446],[0.718,0.826,0.446]]
with open('./csv_data.csv','w') as f:
    for item in a:
        f.write("%s\n"%(','.join([str(i) for i in item])))

with open('./csv_data.csv','a') as f:
    for item in [[1.233,1.973,1.545,1.098],[1.728,1.324,1.873]]:
        f.write("%s\n"%(','.join([str(i) for i in item])))

with open('./csv_data.csv','r') as f:
    data = f.readlines()
    data_chan = []
    for i in data:
        data_chan.append([float(item) for item in i.strip().split(',')])
    print(data_chan)
    print(data)



def print_som(data,num):
    for i in range(num):
        print("%s "%data,end='',flush=True)
        time.sleep(0.1)

print_som('*',30)
