"""
封装
"""
"""class MsgManagerment():
    def __send_v_code(self,code):
        print("发送验证码%s"% code)
    def send_msg(self,type,code):
        if type=="1":
            print("*************")
            self.__send_v_code(code)
            return 0
        else:
            return("没权限")
m=MsgManagerment()
m.send_msg("1","sad")
#print(res)"""
class Person:
    #def __init__(self,name):
        #self.name=name
    def __eat(self,food):
        print("吃：%s"% food)
    def ni(self,ss,food):
        if ss=="1":
            self.__eat(food)
        else:
            return "吃不了"

u=Person()
u.ni("1","苹果")
