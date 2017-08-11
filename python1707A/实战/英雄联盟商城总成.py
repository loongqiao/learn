"""
这是 一个英雄联盟的小超市
可以实现很多意想不到的功能
只有你想不到
没有它做不到
系统还在完善
"""
#导入部分必要模块
import os
import sys
import math
import random
#定义一个列表用来存储注册的账号密码
opra1=["+","-","*","/","//","**"]
opra2=["sin","cos","tan","cot"]
#定义一个空列表用来存放历史纪录
iusers=[]
users=[]
while True:
	os.system("cls")
#打印主菜单

	print("--------------------------------------------------------------------------")
	print("\t\t\t主菜单")
	print(" ")
	print("\t\t1.用户登录")
	print("\t\t2.用户注册")
	print("\t\t3.退出系统")
	print(" ")
	print("--------------------------------------------------------------------------")

	choice=input("请输入你的选项：")
	if choice=="1":
		username=input("请输入你的账号： ").strip()
		password=input("请输入你的密码：").strip()
		for u in iusers:
			if u[0]==username and u[1]==password:
				input("登录成功,按任意键继续")

				#登录后的界面
				while True:
					print("********************************************************************")
					print("   ")
					print("\t\t1.进入游戏商城")
					print("\t\t2.休闲娱乐小游戏")
					print("\t\t3.科学计算器")
					print("\t\t4.婚姻介绍所 ")
					print("\t\t5.返回上级菜单")
					print(" ")
					print("********************************************************************")
					choice=input("请输入你的选项：")
					
					if choice=='1':
						while True:
							print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
							print("编号    姓名  昵称    价格    库存  描述 \n")
							print("1      纳尔   迷失之牙  4000  100  丛林不会原谅盲目和无知 \n")
							print("2      瑞文   放逐之刃  4000  100  她是残忍高效的战士\n")
							print("3      薇恩   暗夜猎手  4000  100  这个世界不像人们想象的那么美好\n")
							print("4      李青     盲僧      4000  20    我用双手成就你的梦想\n")
							print("5      杰斯   未来守护者 4000  100  武装着睿智与魅力，你的选择没有错\n")
							print("6\t\t退出超市")
							print("~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~*~\n")
							
							choice=input("(温馨提示)请输入您要查看的英雄编号: ")
							if choice=='1':	

	#剔除输入的空格
								while True:	
									print("\t英雄名称：纳尔（史诗）\n")
									print("\t英雄属性：生命值428（+85）/攻击距离125\n")
									print("\t英雄座右铭：一人之行可灭世，众人之看勘可救世\n")
									print("\t英雄价格：4000\n")
									print("\t英雄折扣：9.0\n")
									print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")
									input("按任意键返回上一级菜单")
									break
							elif choice=='2':
								while True:
									print("\t英雄名称：瑞文（史诗）\n")
									print("\t英雄属性：生命值428（+85）/攻击距离125\n")
									print("\t英雄座右铭：断剑重铸之日，骑士归来之时\n")
									print("\t英雄价格：4000\n")
									print("\t英雄折扣：9.0\n")
									print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")
									input("按任意键返回上一级菜单")
									break

							elif choice=='3':
								while True:	
									print("\t英雄名称：薇恩\n")
									print("\t英雄属性：生命值428（+85）/攻击距离525\n")
									print("\t英雄座右铭：让我们猎杀那些陷入黑暗中的人吧\n")
									print("\t英雄价格：4000\n")
									print("\t英雄折扣：9.0\n")
									print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")
									input("按任意键返回上一级菜单")

									break

							elif choice=='4':
								while True:
									print("\t英雄名称：盲僧（史诗）\n")
									print("\t英雄属性：生命值428（+85）/能量值200（+0）/移动速度425/攻击力55.9（+3.2）\n\t\t  攻击速度0.651(+3.1%)/护甲值24（+1.25）/攻击距离125\n")
									print("\t英雄座右铭：一人之行可灭世，众人之看勘可救世\n")
									print("\t英雄价格：4000\n")
									print("\t英雄折扣：9.0\n")
									print("插播广告：当风云变色，当流离失所，世界不再是旧日模样\n你是否会为了自己的梦想战斗，直至力战身亡，直至彼岸他乡\n")
									print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")
									input("按任意键返回上一级菜单")
									break

							elif choice=='5':
								while True:
									print("\t英雄名称：杰斯（史诗）\n")
									print("\t英雄属性：生命值428（+85）/攻击距离425\n")
									print("\t英雄座右铭：为了更美好的明天而战\n")
									print("\t英雄价格：4000\n")
									print("\t英雄折扣：9.0\n")
									print("~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~ * ~\n")
									input("按任意键返回上一级菜单")
									break
							elif choice=='6':
								
								break
								

							else:
								print("没有这个选项")


						
					elif choice=='2':
						while True:
							#游戏界面
							print("..............................................................................................................")
							print("\t\t\t休闲娱乐小游戏")
							print("\n")
							print("\t1.老虎棒子鸡")
							print("\t2.猜数字")
							print("\t3.退出系统")
							print("\n")
							print("..............................................................................................................")
							choice=input("请输入你的选项")
							if choice=="1":
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
								x=input("是否继续游戏（继续按任意键，退出游戏按T键）：")
								if x=="T":
									os.system("cls")
									break
								else:
									continue

						

			#系统生成随机数
							elif choice=='2':
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
							elif choice=='3':
								print("系统即将退出.....")
								sys.exit(0)
							else:
								print("没有这个选项")

					elif choice=='3':

						print("----------------------------------------------------------------")
						print(" ")
						print("\t9         8             7            +       sin                                     ")
						print(" ")
						print("\t6         5             4            -        cos                                    ")
						print(" ")
						print("\t3         2             1            *        tan                                     ")
						print(" ")
						print("\t**        0             //           /         cot                                     ")
						print(" ")
						print("----------------------------------------------------------------")
						while True:
							user=[]
							#用户输入第一个数值
							num1=int(input("请输入第一个你要计算的数值："))
							
							#用户输入运算符号
							opration=input("请输入你要运算的符号：")
							
							#定义一个参数，用来存储计算结果
							result=0
							#对输入的运算符号进行判断
							if (opration in opra2)or(opration in opra1):
								#当运算符号位于科学运算时
								if opration in opra2:
									if opration=="sin":
										result=math.sin(math.radians(num1))
									elif opration=='cos':
										result=math.cos(math.radians(num1))
									elif opration=='tan':
										result=math.tan(math.radians(num1))
									elif opration=='cot':
										result=math.cot(math.radians(num1))
								#当运算位于科学运算时
									
								else:
									num2=int(input("请输入你需要的第二个数值："))
									
									#str(num2).append(user)
									if opration=='+':
										result=num1+num2
									elif opration=='-':
										result=num1-num2
									elif opration=='*':
										result=num1*num2
									elif opration=='/':
										result=num1/num2
									elif opration=='//':
										result=num1//num2
									else:
										result=num1**num2
								a="="
								z=str(num1)+opration+str(num2)+a+str(result)	
								user.append(z)
								users.append(user)
								#打印输出结果
								print("您计算的结果为：%s"%result)
								x=input("按Q键退出计算机,按W键查看历史纪录，按任意键继续：")	
								if x=="Q":
									break
								elif x=="W":
									for u in users:
										print(u)					
									
								else:
									continue
					#数据操作页面
					elif choice=='4':
						print("--------------------------------------------------------------------------")
						print("\t\t欢迎来到世纪佳缘")
						print("\t\t1.浏览系统中存在的所有姑娘")
						print("\t\t2.添加一个姑娘")
						print("\t\t3.对姑娘的信息进行修改")
						print("\t\t4.删除一个姑娘")
						print("\t\t5.查看一个特定的姑娘")
						print("\t\t6.返回上一级菜单")
						print("--------------------------------------------------------------------------")

						#定义一个空列表，用来存储姑娘的信息
						girls=[]
						while True:
							#用户选择
							choice=input("请输入你的选项：")
							if choice=='1':
								for name in girls:
									print("姑娘：%s"% name)
									#添加姑娘信息
							elif choice=='2':
								name=input("输入你要添加姑娘的姓名：")
								girls.append(name)
								#查询姑娘信息
							elif choice=='3':
								name=input("请输入你修改姑娘的名字：")
								#判断姑娘是否在list中
								if name in girls:
									#查找姑娘的序列
									index=girls.index(name)
									if index>=0:
										name=input("请输入新的姑娘信息：")
										#将数据存在原来的序列中
										girls[index]=name
								else:
									print("你输错名字了吧")
							#删除选定的姑娘
							elif choice=='4':
								name=input("请输入你要删除的姑娘：")
								#判断姑娘是否在序列中
								if name in girls:
									#删除选定的姑娘
									girls.remove(name)
								else:
									print("查无此人")
							elif choice=='5':
								name=input("请输入你要查看的姑娘：")
								#判断姑娘是否已经存在
								if name in girls:
									print("此姑娘已经存在")
								else:
									print("找不到这个人的信息")
							elif choice=='6':
								break
							else:
								print("没有这个选项，请重新输入")

						
					else:
						print("您的输入有误")
						
						
				



			else:
				input("你输入的账号密码不一致")
				continue

		

	elif choice=="2":
		while True:
		
			username=input("请输入一个账号：").strip()
			password=input("请输入您的密码：").strip()
			passwordagin=input("请再次输入你的密码：").strip()
			if password==passwordagin:
				#定义一个空列表
				luser=[]
				luser.append(username)
				luser.append(password)
				iusers.append(luser)
				input("注册成功，按任意键返回主菜单")
				break
			else:
				input("两次输入不一致，按任意键继续")
				

	elif choice=="3":
		print("系统即将退出.....")
		sys.exit(0)

	else:
		input("没有这个选项，按任意键重新选择")