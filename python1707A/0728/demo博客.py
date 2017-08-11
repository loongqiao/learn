"""
定义全局变量
 定义所需要的类
  程序的入口：__name__=="__main__"
  开发界面对象menu中展示登录界面的函数【用户输入信息(界面)】
    登录界面中->用户输入选项->注册->调用界面的展示注册界面的函数
   开发界面对象Menu中的展示注册界面的函数【用户输入信息（界面）】
    注册界面中->用户输入注册信息->执行注册功能
    注册功能->系统功能,所以在Service(服务)对象中，定义处理注册功能的函数
   开发服务对象Service中，注册功能regist
    开发完成，函数只返回执行结果，不进行界面跳转
     界面对象，根据服务对象返回的执行结果，跳转到不同的展示界面

"""
#引入模块
import time,sys,datetime,pickle
#定义全局变量
users=[]
arts=[]
loginuser=[]

#定义桌面类
class Menu():
    def __init__(self):

        self.sever=Sever()
        self.uu=Utils()


    def showMenu(self):
        print("<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>")
        print("\t\t\t欢迎来到博客系统")
        print("\t\t1.用户登录")
        print("\t\t2.用户注册")
        print("\t\t3.退出系统")
        c=input("请输入你的选项:")
        if c=="1":
            self.ShowLogin()
        elif c=="2":
            self.Showregist()
        elif c=="3":
            print("系统即将退出。。。")
            time.sleep(3)
            sys.exit(0)
    #用户登录
    def ShowLogin(self):
        username = input("请输入你的账号：")
        password = input("请输入你的密码：")
        u=Users(username,password,None)

        self.uu.write()
        res=self.sever.login(u)
        if res:
            self.Showwindow()
        else:
            self.showMenu()
    #用户注册
    def Showregist(self):
        username=input("请输入你的注册账号：")
        for u in users:
            if username==u.username:
                input("您注册的账号已经存在，按任意键重新注册")
                self.Showregist()
        else:
            password=input("请输入你的注册密码：")
            nickname=input("请输入你的昵称：")
            u=Users(username,password,nickname)
        res=self.sever.regist(u)
        if res:
            input("注册成功")
            self.showMenu()
    #新增文章u
    def Addblog(self):
        global arts
        title=input("请输入文章标题：")
        content=input("请输入文章内容：")
        author=loginuser[0][2]
        s=Article(title,content,author)
        print(s)
        res=self.sever.add(s)
        if res:

            self.uu.writes()
            self.Showwindow()
    def Showwindow(self):
        print("<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>")
        print("\t\t\t欢迎进入博客园")
        print("\t\t1.查看所有文章")
        print("\t\t2.查看自己写的文章")
        print("\t\t3.新增一篇博客")
        print("\t\t4.删除一篇博客")
        print("\t\t5.修改一篇博客")
        print("\t\t6.返回主菜单")
        x=input("请输入你的选择：")
        if x=="1":
            self.checkall()

        elif x=="2":
            self.checkself()

        elif x=="3":
            self.Addblog()

        elif x=="4":
            self.delet()
        elif x=="5":
            self.replace()
        elif x=="6":
            self.showMenu()
#删除文章
    def delet(self):
        de=input("请输入你要删除的标题")
        for a in arts:
            if (de==a.title):
                self.sever.dele(a)
                input("删除完成")
                self.Showwindow()

    #查看自己的文章
    def checkself(self):
        global arts
        for a in arts:
            if (loginuser[0][2] == a.author):
                print("标题：%s，内容：%s，作者：%s" % (a.title, a.content, a.author))
                input("查看完毕")
                self.Showwindow()
        else:
            input("您没有发表文章")
            self.Showwindow()
#遍历全部的文章
    def checkall(self):
        global arts
        for p in arts:

            print("标题：%s" % p.title)
            print("内容：%s" % p.content)
            print("作者：%s" % p.author)

            print("--------------------------------------------------")
        print("/////////////////////////////////////////////////////////////")
        input("按任意键返回主菜单")
        self.Showwindow()
#修改文章
    def replace(self):
        p=input("请输入你要修改的标题")
        for u in arts:
            if u.title==p:
                self.sever.dele(u)
                title=input("请输入新的标题")
                content=input("请输入新的内容：")
                author=loginuser[0][2]
                a=Article(title,content,author)
                print(a)
                res = self.sever.add(a)
                self.uu.writes()
                input("修改完成")
                self.Showwindow()

#用户数据
class Users():
    __slots__ = ["__username","__password","__nickname"]
    def __init__(self,username,password,nickname):
        self.__username=username
        self.__password=password
        self.__nickname=nickname
    #注解
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self,zhh):
        self.__username=zhh
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
    def nickname(self,nc):
        self.__nickname=nc
    #打印用户信息
    def __str__(self):
        return "账号:%s,密码：*******,昵称：%s"%(self.username,self.nickname)

#定义文章类
class Article(object):
    __slots__=["__title","__content","__author"]
    def __init__(self, title, content, author):
        self.__title=title
        self.__content=content
        self.__author=author
    #注解
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self,wz):
        self.__title=wz
    @property
    def content(self):
        return self.__content
    @content.setter
    def content(self,nr):
        self.__content=nr
    @property
    def author(self):
        return self.__author
    @author.setter
    def author(self,zz):
        self.__author=zz

    def __str__(self):
        return "标题:%s,内容：%s,作者：%s" % (self.title, self.content,self.author)
#系统处理
class Sever():
    global users,arts,loginuser
    #注册存储
    def regist(self,user):

        users.append(user)
        return True

        # 删除
    def dele(self, a):
        arts.remove(a)

        return True
    #登录判断
    def login(self,user):
        for u in users:
            if (u.username==user.username)\
                    and (u.password==user.password):
                username=u.username
                password=u.password
                nickname=u.nickname
                um = [username, password, nickname]
                loginuser.append(um)
                users.append(um)
                input("登陆成功")
                return True
#添加到arts中
    def add(self,art):
        arts.append(art)
        input("添加成功，按任意键回主菜单")
        return True


#系统写入
class Utils():
    def read(self):
        global users
        try:
            with open("users.dat","br")as f:
                users=pickle.load(f)
        except:
            users=[]

    def write(self):
        with open("users.dat","bw")as f:
            pickle.dump(users,f)
    #文章的数据
    def reads(self):
        global arts
        try:
            with open("arts.dat","br")as f:
                arts=pickle.load(f)
        except:
            arts=[]
    def writes(self):
        with open("arts.dat","bw")as f:
            pickle.dump(arts,f)
#程序的入口
if __name__=="__main__":
    un=Utils()
    un.read()
    u=Utils()
    u.reads()
    menu=Menu()
    menu.showMenu()