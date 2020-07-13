import json

info = [
    {
        "name": "Tom",
        "gender": "male",
        "other": 'None'
    },
    {
        "name": "Jack",
        "gender": "male",
        "other": 'None'
    }
]

# dumps：将数据类型转换成字符串,具体参数含义可以参考内置文档
data = json.dumps(info, indent=4)
print(data)
print(type(data))
