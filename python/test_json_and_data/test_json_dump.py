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

# dump：将数据类型转换成字符串并存储再文件里面
print("读取json文件")
json.dump(info, open("D:\pycharmfile\HogwartsLagoutesting\python\\test_json_and_data\json_dump.json", "w"))

###


