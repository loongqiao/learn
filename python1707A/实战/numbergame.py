"""
猜数字游戏
 系统随机输入一个数字
 玩家进行猜测
 系统会提示你猜大了或者猜小了
 直到猜中为止
 """

 #导入random模块
import random
import sys
import os


while True:
		#打印游戏界面
	print("-----------------------------------------------------------------------------------------------")
	print("\t\t欢迎进入猜数字游戏")
	print("\t\t1.开始游戏")
	print("\t\t2.退出游戏")


	choice=int(input("请输入你的选项："))
	

	#对客户输入的选项进行判断
	if choice==1:
		while True:
		#系统生成随机数
			#定义一个参数用来计算输入的次数
			time=0
			computer=random.randint(0,100)
			print("系统随机生成了一个（1-100）的数字，请您猜测")
		
			while True:
				time+=1
				#用户输入数字
				player=int(input("请您输入数字："))
				#对用户输入的数字进行判断
				if player>computer:
					print("您猜大了，请继续输入")
				elif player<computer:
					print("您猜小了，请继续输入")
				else:
					print("恭喜你猜对了，您一共猜了%s次"% time)
					break
			x=input("是否继续游戏（继续按任意键，退出游戏按T键）：")
			if x=="T":
				os.system("cls")
				break
			else:
				continue
	elif choice==2:
		print("游戏正在退出......")
		sys.exit(0)
	else:
		print("没有这个选项，请重新输入")
		break
