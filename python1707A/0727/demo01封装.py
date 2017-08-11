class Person(object):
    def __init__(self,name):
        self.name=name

p=Person("momo")
print(p,p.name)

p2=p

import sys
print(sys.getrefcount(p))#几个对象引用

del p2
print(sys.getrefcount(p))