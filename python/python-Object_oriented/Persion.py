# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/29 22:27
# @File     : Persion.py
"""
创建一个Persion类
    属性：姓名，性别，年龄，存款金额
    方法：吃，睡。跑。赚钱
"""


class Persion():

    def __init__(self, name, gender, age, money):
        self.name = name
        self.gender = gender
        self.age = age
        self.money = money

    def eat(self):
        print('我再吃东西')

    def sleep(self):
        print('我在睡觉')

    def run(self):
        print("我在跑步")

    def make_money(self):
        print("我在赚钱")
