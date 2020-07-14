"""
捕获异常的处理方法：
1.根据具体异常进行处理
2.不清楚具体异常统一处理
"""



try:
    num1 = int(input("输入一个除数"))
    num2 = int(input("输入一个被除数"))
    print("最终结果：%d" % (num1 / num2))
# except ZeroDivisionError:
#     print("被除数不能为零")
# except ValueError:
    # print("输入的需要是数值类型的整数")
except :
    print("这是一个异常处理")
finally:
    print("是否异常均执行此内容")
