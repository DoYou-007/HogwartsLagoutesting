import pytest
from test_case.adress import Adress

class TestAdress:
    def setup(self):
        self.Adress = Adress()

    @pytest.mark.parametrize('name,userid,mobile',[('阿伯21','helo12',13800000921),
                                                   ('阿伯23','helo13',13800000931),
                                                   ('阿伯25','helo14',13800000941)])
    def test_add_member(self,name,userid,mobile):
        department = [1]
        #数据清理
        self.Adress.delete_member(userid)

        #添加成员
        print(name)
        r=self.Adress.add_member(userid=userid,name=name,mobile=mobile,department=department)
        assert r.get('errcode','其他错误妈') == 0

        #查询是否添加成功
        r = self.Adress.get_member(userid)
        assert r.get('userid','该成员未被添加') == userid


