class Student(object):
    def __init__(self,name,age):
        self.__name=name
        self.__age=age

    def set_name(self,name):
        self.__name=name
    def get_name(self):
        return self.__name
    def set_name(self,age):
        self.__age=age

    def get_age(self):
        return self.__age
p=Student("王小明",26)
print(p.get_name(),p.get_age())
