class Person:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def panduan(self):
        print("[%s]的年龄是【%s】"%(self.name,self.age))

class Man(Person):
    def __init__(self,name,age,sex):
        Person.__init__(self,name,age,sex)

    def panduan(self):
        print("[%s]先生的年龄是【%s】"%(self.name,self.age))

class Women(Person):
    def __init__(self, name, age, sex):
        Person.__init__(self, name, age, sex)
        self.name = name
        self.age = age
        self.sex = sex

    def panduan(self):
        print("%s小姐is %s years old" % (self.name, self.age))
class Nianl:
    def __init__(self):
        self.name="神算子"
    def pan(self,person):
        if isinstance(person,Person):
            if person.age>0 and person.age<18:
                print("未成年")
                person.age+=2
                person.panduan()
            elif person.age>18 and person.age <58:
                print("成年人")
                person.panduan()
                person.age+=15
            else:
                print("老年人")
                person.panduan()


a=Nianl()
ming=Person("小明",15,"男")
hong=Women("rose",22,"女")
wang=Man("wang",65,"man")


a.pan(ming)
a.pan(hong)
a.pan(wang)



