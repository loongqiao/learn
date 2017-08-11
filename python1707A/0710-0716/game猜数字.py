"""
这是一个猜数字的游戏
系统随机输入一个数字
玩家进行猜测 
系统会提醒玩家猜大/小了
直到玩家猜中 系统会计算玩家进行的次数
"""
#导入随机数模块
import random
#导入os模块
import os
os.system('cls')
print("@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.")
print("@                                                 猜数字                                                                                                                                                               @")
print("@                                    系统随机输入一个数字                                                                                                                                                              @")
print("@                               玩家进行猜测 系统会提醒猜大/小了                                                                                                                                                       @")
print("@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.@.")

while True:
#系统随机输入一个数字
	computer=random.randint(0,100)
	time=0
	print("系统随机输入了一个100内的数，请您进行猜测")

	while True:
			#用户进行猜测
		guess=int(input("请输入你猜测的数字： "))
		time +=1
			#对用户输入的数字进行判断
		if guess > computer :
			print("您猜大了")
		elif guess<computer :
			print("您猜小了")
		else:
			print("恭喜您，猜对了。您一共猜了%d 次。"% time)
			break
	goon=input("是否继续进行游戏Y/N：")
	if  goon=='N':
		os.system('cls')
		break
	if  goon=='Y':
		continue


