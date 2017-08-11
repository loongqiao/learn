"""
这是一个石头剪刀布的游戏
玩家和电脑进行对战 
玩家输入0为石头 1为剪刀  2为布 电脑随机输入
"""
#导入随机数模块
import random
#玩家输入
player=input("请亮出你的绝招吧(0为石头，1为剪刀，2为布): ")
#数据类型转换
player=int(player)
#电脑随机输入
computer=random.randint(0,2)
if (player==0 and computer == 1)or (player==1 and computer==2)or (player==2 and computer==0):
	print("恭喜你，胜利了")
elif (player==computer):
	print("平局")
else:
	print("bingo,你输了，再接再厉！")
