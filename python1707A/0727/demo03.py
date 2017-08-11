#方法重载：
#在一个类型中，出现了名称相同，不同参数的函数|方法，
#称为方法的重载。
#目的：在执行的过程中，通过参数的不同，来执行不同的代码，实现不同的功能

class Person:
    def __init__(self,name):
        self.__name=name
    @property
    def get_name(self):
        return self.__name
    @get_name.setter
    def set_name(self,name):
        self.__name=name

p=Person("ss")
print(p.get_name)
p.name="hh"
print(p.name)