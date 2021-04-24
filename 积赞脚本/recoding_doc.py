# coding=utf-8

# @Software : PyCharm

#Python学习群827513319

import sys

from PyQt5.QtCore import *

from PyQt5.QtWidgets import *

import time

#mac下没有pywin32的第三方库
import win32api,win32con

from recode_sex import Recording,StopRecording

class WorkThread(QThread):

    def __init__(self, n):

        super(WorkThread, self).__init__()
        self.n = n

    def run(self):

        if self.n == 1:
            Minimize_Window()
            Recording(1)

        elif self.n == 2:

            Minimize_Window()
            Recording(2)

        else:
            StopRecording()

def Minimize_Window():

    win32api.keybd_event(91, 0, 0, 0)
    time.sleep(0.5)

    win32api.keybd_event(40, 0, 0, 0)
    time.sleep(0.5)

    win32api.keybd_event(91, 0, win32con.KEYEVENTF_KEYUP, 0)
    win32api.keybd_event(40, 0, win32con.KEYEVENTF_KEYUP, 0)

class Ui_Mainwindow():

    def setupUi(self, top):

    # 垂直布局类QVBoxLayout

        layout = QVBoxLayout(top)

    # 添加录屏相关按钮

        button1 = QPushButton("自定义录屏")

        layout.addWidget(button1)

        button2 = QPushButton("全屏录屏")

        layout.addWidget(button2)

        button3 = QPushButton("停止录屏")

        layout.addWidget(button3)

        self.text = QPlainTextEdit('欢迎使用！')

        layout.addWidget(self.text)

        button1.clicked.connect(lambda: self.work(1))

        button2.clicked.connect(lambda: self.work(2))

        button3.clicked.connect(lambda: self.work(3))

    def work(self, n):

        if n == 1 :

            print('已选择自定义录屏：')

            self.text.setPlainText('正在录屏中，请等待……')

        elif n == 2 :

            print('已选择全屏录屏：')

            self.text.setPlainText('正在录屏中，请等待……')

        else:

            print('已选择结束录屏：')

            self.text.setPlainText('录屏结束！(点击关闭按钮，可退出程序！)')

        self.workThread = WorkThread(n)

        self.workThread.start()

if __name__ == "__main__":

    app = QApplication(sys.argv)

    top = QWidget()

    top.setWindowTitle('录屏小工具')

    top.resize(300, 170)

    ui = Ui_Mainwindow()

    ui.setupUi(top)

    top.show()

    sys.exit(app.exec_())# coding=utf-8

