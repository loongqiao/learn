﻿import os
#首界面内容
print("\t\t英雄联盟商城首页\n")
print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*\n")
print(" \n")
print("\t\t1.进入英雄超市\n")
print("\t\t2.休闲小游戏\n")
print("\t\t3.退出登录\n")
print("\n")
choice=input("(温馨提示)请输入您的选项:")

#英雄价格介绍
if choice=='1':
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
    print("编号    姓名  昵称    价格    库存  描述 \n")
    print("1      纳尔   迷失之牙  3500  100  丛林不会原谅盲目和无知 \n")
    print("2      瑞文   放逐之刃  4000  100  她是残忍高效的战士\n")
    print("3      薇恩   暗夜猎手  3500  100  这个世界不像人们想象的那么美好\n")
    print("4      李青     盲僧      4800   20    我用双手成就你的梦想\n")
    print("5      杰斯   未来守护者 2500  100  武装着睿智与魅力，你的选择没有错\n")
    print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
    choice=input("(温馨提示)请输入您要查看的英雄编号: ")

#英雄属性介绍
    if choice=='4':
        print("\t英雄名称：盲僧（史诗）\n")
        print("\t英雄属性：生命值428（+85）/能量值200（+0）/移动速度425/攻击力55.9（+3.2）\n\t\t  攻击速度0.651(+3.1%)/护甲值24（+1.25）/攻击距离125\n")
        print("\t英雄座右铭：一人之行可灭世，众人之看勘可救世\n")
        print("\t英雄价格：4800\n")
        print("\t英雄折扣：9.5\n")
        print("插播广告：当风云变色，当流离失所，世界不再是旧日模样\n你是否会为了自己的梦想战斗，直至力战身亡，直至彼岸他乡\n")
        print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")
        choice=input("请输入你要购买的英雄： ")

#英雄购买详情介绍
        if choice=='4':
            print("英雄购买票据\n")
            print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
            print("    \n")
            print("\t英雄名称：李青（史诗）\n")
            print("\t英雄昵称：盲僧")
            print("\t英雄价格：4800\n")
            print("\t活动折扣：9.0\n")
            print("\n")
            choice=input("出示会员卡： ")
            if choice=='YES':
                print("\t应付付款：4320\n")
                print("\t实际付款：5000\n")
                print("\t找零：680\n")
                print("\n")
            else:
                print("\t应付付款：4800\n")
                print("\t实际付款：5000\n")
                print("\t找零：200\n")
                print("插入广告：\n")
                print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
            choice=input("(温馨提示）按数字'ESC'键退出系统: ")
            if choice=='ESC':
                os.system('cls')            
