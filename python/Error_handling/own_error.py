# x = 20
# if x > 5:
#     raise Exception("这里抛出的是异常信息")


class MyExecption(Exception):
    def __init__(self,value1,value2):
        self.value1 = value1
        self.value2 = value2

raise MyExecption("value1","value2")