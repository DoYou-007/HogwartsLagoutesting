 #fixture 类似于setup teardown 的测试装置
import pytest


# pytest 测试装置
# scope="class"  相当于 setup_class

# fixture 用法：
# 1. 可以通过 方法名字传递到测试用例的参数中，进行调用
# 2. 使用return 关键字返回数据
# 3. 使用fixture 的名字来调用返回数据
# 4. yield 来激活 teardown 的操作

#
@pytest.fixture(scope="class",autouse=True)
def login():
    # setup
    print("准备登录")
    # yield相当于 return , 暂停，记住上一次的执行位置
    yield "username,password"
    # teardown
    print("登出操作")

@pytest.fixture
def conndb():
    print("connect database")


class TestDemo1:
    def test_demo1(self, login, conndb):
        print(f"登录信息：{login}")
        print("demo1")

    def test_demo2(self, login):
        print(f"登录信息：{login}")
        print("demo2")