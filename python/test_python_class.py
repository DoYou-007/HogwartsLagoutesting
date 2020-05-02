class People:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def fit(self,value):
        print(f"{self.name} is {value}")


    def eat(self):
        print(f"name: {self.name},age : {self.age}, gender :{self.gender}", "在吃饭")

    def drink(self):
        print(f"name: {self.name},age : {self.age}, gender :{self.gender}", "在喝水")

    def run(self):
        print(f"name: {self.name},age : {self.age}, gender :{self.gender}", "在跑步")


xiaohong = People('xiaohong', 20, 'male')
xiaoming = People('xiaoming', 23, 'female')

print(xiaohong.name)    #获取对象的属性
xiaohong.eat()        #使用类的方法

xiaohong.fit('fit')        #其他属性可以通过方法的方式增加