class Student:
    def __init__(self,name,age):
        self.__name=name
        self.__age=age
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self,n):
        self.__name=n
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self,m):
        self.__age=m
a=Student("wo",33)
print(a.name,a.age)
a.name="ni"
a.age="44"
print(a.name,a.age)