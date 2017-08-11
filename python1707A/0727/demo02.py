"""class Person(object):
    def __init__(self,name):
        self.__name=name
    def get_name(self):
        return self.__name

    def __set_name__(self,name):
        self.__name=name
    def eat(self):
        print("吃")
    def drink(self):
        print("喝")

p=Person("小明")
#p.eat()
#p.drink()
print(p.get_name())"""
#V2.0
class Student():
    def __init__(self,name):
        self.__name=name

    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def set_name(self,name):
        self.__name=name
p=Student("hi")
print(p.get_name)
p.set_name="hello"
print(p.get_name)