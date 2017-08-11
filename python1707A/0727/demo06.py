class Person():
    def __init__(self,name):
        self.name=name
    def eat(self,food):
        print(self.name+"吃饭了，吃的是%s"%food)
    def run(self,m):
        print(self.name+"跑了%s米"%m)
class Son(Person):
    def __init__(self,name):
        self.name=name
    def run(self,m):
        print(self.name + "跑了%s千米" % m)


a=Person("李华")
a.eat("盖浇饭")
a.run("50000")
b=Son("张飞")
b.eat("面")
b.run("40000")