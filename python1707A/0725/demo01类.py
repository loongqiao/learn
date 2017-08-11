'''
定义一个 用户类型
    抽象
        类名称
        类属性
        类行为
        类的声明：
        class 类名称：#声明了一个类[自定义了一个类型]

            #定义类的属性[变量]->在面向对象编程中，对象的属性称为成员变量
            def __init__(self,参数列表)
                self.属性=参数
            #定义类的行为[函数]->在面向对象编程中，对象的函数称为成员方法
            def 方法名称(我)：
                方法执行的代码
        类-> 对象-->变量+函数

        面向对象：就是将生活中的对象抽象到程序中
        生活中的对象，就是把生活中的思想抽象到程序中

    1.面向对象：类和对象、类的方法的使用

    2.面向对象的第一个特征：封装

    3.面向对象的第二个特征：继承

    4.面向对象的第三个特征：多态
'''


#定义一个用户类
class Users:
    def __init__(self,username,password,nickname):
        self.username=username
        self.password=password
        self.nickname=nickname

    def eat(self):
        print(self.nickname+"早吃饭")

    def sleep(self):
        print(self.nickname+"去开房了。。。")

    def play_game(self):
        print(self.nickname+"去玩耍了")

#创建类型对应的实际存在的物体
u1=Users("admin","admin","oldwang")
print(u1.username,u1.password,u1.nickname)
u1.eat()
u1.sleep()
u1.play_game()

u2=Users("manager","manager","oldli")
print(u2.username,u2.password,u2.nickname)
u2.eat()
u2.sleep()
u2.play_game()