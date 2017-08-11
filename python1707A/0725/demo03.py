class User:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
    def eat(self):
        print(self.name+"去上课")

    def play(self):
        print(self.name+"打游戏")

u=User("wangxiaoming","17","男")
print(u.name,u.age,u.sex)
u.eat()
u.play()