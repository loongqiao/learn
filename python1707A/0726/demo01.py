class Person(object):
    def __init__(self):
        self.bing="冰箱"
        self.__baoxianxiang = "保险箱"
        self._tv="电视机"


    def set_baoxianxiang(self,bxx):
        set.__baoxianxiang=bxx

    def get_baoxianxiang(self):
        return  self.__baoxianxiang

p=Person()
print(p.bing)
print(p._tv)
print(p.get_baoxianxiang())
#print(p.__baoxianxiang)
