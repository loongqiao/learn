"""
娶妻嫁夫
"""
#定义类
class Person(object):
    #定义类的属性
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.mate=None
        self.type=None

        # 字符串转换
    def __str__(self):
        return "姓名:%s；年龄：%s；性别：%s；配偶：[%s];类别：%s" \
               % (self.name, self.age, self.sex, self.mate, self.type)

    def marry(self,person):
        if self.sex == "男":
            self.type = "娶妻"
        else:
            self.type= "入赘"
        self.mate=person
        person.mate=self.name
        person.type=self.type


#创建对象
if __name__=="__main__":
    """rose=Person("露丝",21,"女")
    jack=Person("杰克",23,"男")
    jack.marry(rose)
    print(jack)
    rose.marry(jack)
    print(rose)"""
    name1=input("请输入姓名：")
    age1=input("请输入年龄：")
    sex1=input("请输入性别：")
    name2=input("请输入姓名：")
    age2=input("请输入年龄：")
    sex2=input("请输入性别：")
    name3=Person(name1,age1,sex1)
    name4=Person(name2,age2,sex2)
    name3.marry(name4)
    print(name3)

