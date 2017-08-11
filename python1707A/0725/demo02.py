class Student:
    def __init__(self,name,grade,sex):
        self.name=name
        self.grade=grade
        self.sex=sex

    def eat(self):
        print(self.name+"去吃饭了")

    def shangke(self):
        print(self.name+"去上课")

    def play(self):
        print(self.name+"打游戏去")

u=Student("王小明","Pythin1707A","男")
print(u.name,u.grade,u.sex)
u.eat()
u.shangke()
u.play()