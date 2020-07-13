import json

# load 将文件打开从字符串转化成json

jsOBj = json.load(
    open("D:\pycharmfile\HogwartsLagoutesting\python\\test_json_and_data\\test.json", "r", encoding="utf-8"))
print(jsOBj)
print(type(jsOBj))
print(jsOBj[0]['title'])
