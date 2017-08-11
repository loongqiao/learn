﻿#导入OS模块
import os

#首界面内容
print("\t\t英雄联盟商城首页\n")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n")
print(" \n")
print("\t\t1.进入英雄超市\n")
print("\t\t2.休闲小游戏\n")
print("\t\t3.退出登录\n")
print("\n")
choice=input("(温馨提示)请输入您的选项:")
choice=choice.strip()
#剔除输入的空格
if  choice.isdigit:
#判断输入的是否合法
#英雄价格介绍
    if choice=='1':
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
        print("编号    姓名  昵称    价格    库存  描述 \n")
        print("1      纳尔   迷失之牙  4000  100  丛林不会原谅盲目和无知 \n")
        print("2      瑞文   放逐之刃  4000  100  她是残忍高效的战士\n")
        print("3      薇恩   暗夜猎手  4000  100  这个世界不像人们想象的那么美好\n")
        print("4      李青     盲僧      4000  20    我用双手成就你的梦想\n")
        print("5      杰斯   未来守护者 4000  100  武装着睿智与魅力，你的选择没有错\n")
        print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
    #英雄属性介绍
        choice=input("(温馨提示)请输入您要查看的英雄编号: ")
        choice=choice.strip()
    #剔除输入的空格
        if  choice.isdigit:
#判断输入的是否合法
            if choice=='1':
                print("\t英雄名称：纳尔（史诗）\n")
                print("\t英雄属性：生命值428（+85）/攻击距离125\n")
                print("\t英雄座右铭：一人之行可灭世，众人之看勘可救世\n")
                print("\t英雄价格：4000\n")
                print("\t英雄折扣：9.0\n")
                print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")

            if choice=='2':
                print("\t英雄名称：瑞文（史诗）\n")
                print("\t英雄属性：生命值428（+85）/攻击距离125\n")
                print("\t英雄座右铭：断剑重铸之日，骑士归来之时\n")
                print("\t英雄价格：4000\n")
                print("\t英雄折扣：9.0\n")
                print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")

            if choice=='3':
                print("\t英雄名称：薇恩\n")
                print("\t英雄属性：生命值428（+85）/攻击距离525\n")
                print("\t英雄座右铭：让我们猎杀那些陷入黑暗中的人吧\n")
                print("\t英雄价格：4000\n")
                print("\t英雄折扣：9.0\n")
                print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")

            if choice=='4':
                print("\t英雄名称：盲僧（史诗）\n")
                print("\t英雄属性：生命值428（+85）/能量值200（+0）/移动速度425/攻击力55.9（+3.2）\n\t\t  攻击速度0.651(+3.1%)/护甲值24（+1.25）/攻击距离125\n")
                print("\t英雄座右铭：一人之行可灭世，众人之看勘可救世\n")
                print("\t英雄价格：4000\n")
                print("\t英雄折扣：9.0\n")
                print("插播广告：当风云变色，当流离失所，世界不再是旧日模样\n你是否会为了自己的梦想战斗，直至力战身亡，直至彼岸他乡\n")
                print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")

            if choice=='5':
                print("\t英雄名称：杰斯（史诗）\n")
                print("\t英雄属性：生命值428（+85）/攻击距离425\n")
                print("\t英雄座右铭：为了更美好的明天而战\n")
                print("\t英雄价格：4000\n")
                print("\t英雄折扣：9.0\n")
                print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")

        #选择你要购买的英雄序号
            choice=input("请选择你要购买的英雄序号： ")
            choice=choice.strip()
        #剔除输入的空格
            if  choice.isdigit:
    #判断输入的是否合法
        #英雄购买详情介绍
                if choice=='1':
                    print("英雄购买票据\n")
                    print("\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
                    print("\t英雄名称：纳尔\n")
                    print("\t英雄昵称：迷失之牙")
                    print("\t英雄价格：4000\n")
                    print("\t活动折扣：9.0\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

                if choice=='2':
                    print("英雄购买票据\n")
                    print("\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
                    print("\t英雄名称：瑞文（史诗）\n")
                    print("\t英雄昵称：放逐之刃")
                    print("\t英雄价格：4000\n")
                    print("\t活动折扣：9.0\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

                if choice=='3':
                    print("英雄购买票据\n")
                    print("\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
                    print("\t英雄名称：薇恩\n")
                    print("\t英雄昵称：暗夜猎手")
                    print("\t英雄价格：4000\n")
                    print("\t活动折扣：9.0\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

                if choice=='4':
                    print("英雄购买票据\n")
                    print("\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
                    print("\t英雄名称：李青（史诗）\n")
                    print("\t英雄昵称：盲僧")
                    print("\t英雄价格：4000\n")
                    print("\t活动折扣：9.0\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

                if choice=='5':
                    print("英雄购买票据\n")
                    print("\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
                    print("\t英雄名称：杰斯\n")
                    print("\t英雄昵称：未来守护者")
                    print("\t英雄价格：4000\n")
                    print("\t活动折扣：9.0\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

            #会员卡优惠活动
                price=input("出示会员卡： ")
                price=price.strip()
            #剔除输入的空格
                if price=='YES':
                    print("\t应付付款：3600\n")
                    print("\t实际付款：4000\n")
                    print("\t找零：400\n")
                    print("\n")
                else:
                    print("\t应付付款：4000\n")
                    print("\t实际付款：5000\n")
                    print("\t找零：1000\n")
                    print("插入广告：会员大促销存5000送1000\n")
                    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")

                    #退出系统详情
                    choice=input("(温馨提示）按数字'ESC'键退出系统: ")
else:
    print("您的输入有误，系统强制退出！！")        
                      