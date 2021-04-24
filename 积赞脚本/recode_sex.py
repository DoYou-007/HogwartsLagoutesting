# 2、录屏函数

# coding=utf-8

# @Software : PyCharm
import jpype
from PIL import ImageGrab
import numpy as np
import cv2
import os

def Recording(tag=1):

# 录屏开始时创建test.txt,作为结束录屏的条件

    if not os.path.exists('test.txt'):

        f = open('test.txt', 'w')
        f.close()

    # 根据tag值判断自定义录屏或全录屏

    if tag == 1:
        r = SelectRegion()
        record_region = (r.x, r.y, r.w + r.x, r.h + r.y) # 自定义录屏的范围(左上坐标、右下坐标)

    elif tag == 2:

        record_region = None

        image = ImageGrab.grab(record_region) # 获取指定范围的屏幕对象

        width, height = image.size

        fourcc = cv2.VideoWriter_fourcc(*'XVID')

        video = cv2.VideoWriter('test.avi', fourcc, 25, (width, height)) # 默认视频为25帧

        while True:
            captureImage = ImageGrab.grab(record_region) # 抓取指定范围的屏幕

            frame = cv2.cvtColor(np.array(captureImage), cv2.COLOR_RGB2BGR)

            video.write(frame) # 将每帧画面写视频文件

# 停止录屏的条件：test.txt被删除

            if not os.path.exists('test.txt'):
                break

            video.release()

        cv2.destroyAllWindows()

def SelectRegion():

    jvmPath = jpype.get_default_jvm_path()

    jpype.startJVM(jvmPath, '-ea', '-Djava.class.path=F:\\sikuli\\1\\sikulixapi.jar') #加载jar包路径

    Screen = jpype.JClass('org.sikuli.script.Screen')

    myscreen = Screen()

    region = myscreen.selectRegion() # 自定义获取屏幕范围

    return region

def StopRecording():
    os.remove('test.txt') #停止录屏的触发条件

if __name__ == "__main__":
    Recording()