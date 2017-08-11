class Eat():
    def __init__(self,name):
        self.name=name
    def Food(self,fod):
        print("吃饭了，吃的是%s"%fod)
class Person(Eat):
    def Food(self,fod):
        print("去吃饭，吃的是%s"%fod)

x=Person("a")
x.Food("米")
y=Eat("sds")
y.Food("面")
