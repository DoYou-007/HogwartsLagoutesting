# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/14 13:32
# @Author   : XFbeibei.
# @File     : Example_class.py
# @Software : PyCharm

class Persion:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def set_att(self, value):
        self.value = value

    def eat(self):
        print(f"name : {self.name} ,age : {self.age} ,gender : {self.gender} 我在吃饭")

    def drink(self):
        print(f"name : {self.name} ,age : {self.age} ,gender : {self.gender} 我在喝酒")

    def run(self):
        print(f"name : {self.name} ,age : {self.age} ,gender : {self.gender} 我在跑步")


xiaoming = Persion('xiaoming', 23, 'male')
xiaohong = Persion("xiaohong", 34, 'fenale')

xiaohong.eat()
xiaoming.set_att('fit')
print(xiaoming.value)
# print(xiaohong.value)
