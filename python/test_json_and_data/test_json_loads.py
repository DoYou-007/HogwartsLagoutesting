import json

# loads 将字符串转成json

str = '''
[{
        "name":"Tom",
        "gender":"male",
        "other":'None'
    },
    {
        "name":"Jack",
        "gender":"male",
        "other":'None'
}]
'''

print(type(str))
data = json.loads(str)
print(data)
print(type(data))

##未跑通 1
