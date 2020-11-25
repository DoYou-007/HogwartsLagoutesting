# _*_ coding: UTF-8 _*_
# @Time     : 2020/7/29 22:11
# @File     : main.py

have_girl = False


def send():
    print("发女朋友啦。。")
    global have_girl
    have_girl = True
    print(f"have_girl = {have_girl}")


def show():
    if have_girl == True:
        print("有女朋友了，好开心 --")
    else:
        print("单身贵族 ***")
