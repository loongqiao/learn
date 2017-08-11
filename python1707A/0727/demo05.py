class Person:
    # 2.类属性：类变量~定义在类的内部，方法的外部的属性
    # 当前类创建的对象所公共使用
    onlineCount = 100

    def __init__(self, name):
        # 3.成员属性：当前创建的对象的独立数据，不能被其他对象访问
        self.name = name

    def eat(self, money):
        # 4. 局部变量：声明在函数的参数/内部，函数执行时变量创建，函数执行完成，变量销毁
        if money > 10 and money < 15:
            print("鱼香肉丝")
            print("回锅肉")
            print("木耳肉片")
            print("宫保鸡丁")
        elif money > 20:
            print("大盘鸡")
        elif money > 50:
            print("烤全羊")
u=Person("asdas")
u.eat(12)