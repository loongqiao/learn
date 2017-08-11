"""
博客系统
开发步骤：
    1.先定义全局变量：users和articles
    2.定义需要的类：class Menu和class user和class service
    3.定义程序的入口：__name__=="__main__"：调用
    展示登录界面的函数和界面站西相关的，都定义在menu类型中
    4.开发界面对象menu中展示登录界面的函数【用户输入信息(界面)】
    登录界面中->用户输入选项->注册->调用界面的展示注册界面的函数
    5.开发界面对象Menu中的展示注册界面的函数【用户输入信息（界面）】
    注册界面中->用户输入注册信息->执行注册功能
    注册功能->系统功能,所以在Service(服务)对象中，定义处理注册功能的函数
    6.开发服务对象Service中，注册功能regist
    开发完成，函数只返回执行结果，不进行界面跳转
    7. 界面对象，根据服务对象返回的执行结果，跳转到不同的展示界面

"""
#定义全局变量
users=[]
arts=[]
loginuser=[]

import pickle
#登录主页面
class Menu(object):
    def __init__(self):
        self.sever=Service()
        self.uu=Utils()
    def showLoginMenu(self):
        print(users)
        print("///////////////////////////////////////")
        print("\t\t欢迎登陆博客")
        print("\t\t1.用户登录")
        print("\t\t2.用户注册")
        print("\t\t3.退出系统")
        print("///////////////////////////////////////")
        c=input("请输入你的选项：")
        if c=="1":
            print(users)
            usename=input("请输入账号")
            password=input("请输入密码")
            u=Users(usename,password,None)
            self.uu.write()
            res=self.sever.login(u)
            if res:
                self.showmain()
            else:
                self.showLoginMenu()
        elif c=="2":
            self.showregist()
        elif c=="3":
            pass
        else:
            input("没有这个选项，按任意键继续")
            self.showLoginMenu()



        #定义注册函数
    def showregist(self):
        usename=input("请输入你要注册的账号：")
        password=input("请输入你要注册的密码")
        nickname=input("请输入昵称：")
        #开始注册
        u=Users(usename,password,nickname)
        print(u)
        res=self.sever.regist(u)
        if res:
            input("用户注册成功，按任意键返回")
            self.showLoginMenu()

    def showmain(self):
        print("登陆成功")




#用户类
class Users(object):
    __slots__ = ["__usename","__password","__nickname"]

    #定义初始化数据
    def __init__(self,usename,password,nickname):
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
    %(self.__usename,self.nickname)

class Article(object):
    __slots__ = ["__title", "__content", "__author"]

    def __init__(self, title, content, author):
        self.__title = title
        self.__content = content
        self.__author = author

        # 注解
        @property
        def title(self):
            return self.__title

        @title.setter
        def title(self, wz):
            self.__title = wz

        @property
        def content(self):
            return self.__content

        @content.setter
        def content(self, nr):
            self.__content = nr

        @property
        def author(self):
            return self.__author

        @author.setter
        def author(self, zz):
            self.__author = zz

        def __str__(self):
            return "标题:%s,内容：%s,作者：%s" % (self.title, self.content, self.author)


#系统业务处理
class Service():
    global users,loginuser
    #用户注册
    def regist(self,user):
        users.append(user)
        return True

    #用户登录
    def login(self,user):
        for u in users:
            if (u.usename==user.usename)\
                and(u.password==user.password):
                input("登陆成功")
                return True
        else:
            input("登录失败")
            return False

#添加
    def add(self, art):
        arts.append(art)
        input("添加成功，按任意键回主菜单")
        return True

#数据读写类
class Utils(object):
    def read(self):
        global users
        try:
            with open("users.dat","br")as f:
                users=pickle.load(f)
        except:
            users=[users]

    def write(self):
        with open("users.dat","bw")as f:
            pickle.dump(users,f)



#程序的入口
if __name__=="__main__":
    #启动程序
    un=Utils()
    un.read()
    menu=Menu()#界面对象
    menu.showLoginMenu()#展示登陆界面



