"""
烤牛排
"""
class Beef(object):
    #如果创建对象的时候，对象的某些属性就具备固定的值，此时不需要传递参数直接使用默认值即可
    def __init__(self):
        self.cookedDesc="生的"
        self.cookedInt=0
        self.seasoning=[]#调料

    #定义一个天加佐料的方法
    def addSeasoning(self,s):
        self.seasoning.append(s)
    #字符串转换 解决输出只显示内存问题
    def __str__(self):
        return "熟度：%s;烧烤时间：%s;佐料：%s;"%(self.cookedDesc,self.cookedInt,self.seasoning)

    #定义一个烧烤的行为
    def bbq(self,time):
        self.cookedInt += time
        if(self.cookedInt>0)and(self.cookedInt<=2):
            self.cookedDesc="一分熟"
        elif(self.cookedInt>2)and(self.cookedInt<=5):
            self.cookedDesc="三分熟"
        elif(self.cookedInt>5)and(self.cookedInt<=7):
            self.cookedInt="五分熟"
        elif(self.cookedInt>7)and(self.cookedInt<=9):
            self.cookedInt="八分熟"
        elif(self.cookedInt>9)and(self.cookedInt<=12):
            self.cookedInt="熟透了"
        elif self.cookedInt>12:
            self.cookedInt="烤糊了"

#python中的main方法：表示下面的代码只能执由当前文件执行
if __name__=="__main__":
    beef=Beef()
    beef.bbq(1)
    beef.addSeasoning("黄油")
    print(beef)
    beef.bbq(1)
    print(beef)

    beef.bbq(1)
    print(beef)


    beef.bbq(1)
    beef.addSeasoning("意面")
    print(beef)
    beef.bbq(1)
    print(beef)
    beef.bbq(1)
    beef.addSeasoning("黑椒")
    print(beef)




