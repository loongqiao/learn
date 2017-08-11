"""
这是一个老虎棒子鸡的游戏
老虎吃鸡 鸡吃虫 虫啄棒子 棒子打老虎
老虎=0
鸡=1
虫=2
棒子=3
"""

#导入random模块
import random

#用户输入
plyer=input("请您出招(0为老虎，1为鸡，2为虫，3为棒子)： ")

#电脑随机出招
computer=random.randint(0,3);

#判断胜负
if (plyer=='0' and computer== '1')or (plyer=='1' and computer== '2')or (plyer=='2' and computer== '3')or (plyer=='3' and computer== '0'):
	print("恭喜你获得胜利")
elif(computer=='0' and plyer=='1')or(computer=='1' and plyer=='2')or(computer=='2' and plyer=='3')or(computer=='3' and plyer=='0'):
	print("Bingo,你输了，干了这一杯吧！")
else:
	print("平局")