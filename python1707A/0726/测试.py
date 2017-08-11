ef showregist(self):
        usename=input("请输入你要注册的账号：")
        password=input("请输入你要注册的密码")
        nickname=input("请输入昵称：")
        #开始注册
        u=Users(usename,password,nickname)
        res=self.s.regist(u)
        if res:
            input("用户注册成功，按任意键返回")
            self.showLoginMenu()




#用户类
class Users():
    __slots__ = ["__usename","__password","__nickname"]

    #定义初始化数据
    def __init(self,usename,password,nickname):
        self.__usename=usename
        self.__password=password
        self.__nickname=nickname

    @property
    def usename(self):
        return self.__usename

    @usename.setter
    def usename(self,zh):
        self.__usename=zh

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self,mm):
        self.__password=mm

    @property
    def nickname(self):
        return self.__nickname

    @nickname.setter
    def nickname(self,mz):
        self.__nickname=mz
    #打印用户信息
    def __str__(self):
        return "账号：%s，密码：******，昵称：%s"\
    %(self.__usename,self.__password,self.nickname)