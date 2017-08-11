class Person():
    def __init__(self,name):
        self.name=name
    def eat(self):
        print("吃喝拉撒")
    def study(self):
        print("毕业了")

class Student(Person):
    def student(self):
        print("好好学习，天天向上")

u=Person("亚当")
u.eat()
u.study()
p=Student("小明")
p.eat()
p.student()
