"""
宠物大乱斗
"""
#导入系列模块
import os
import sys
pets=[]

users=[]

while True:
	print("┍----------------------------------------------------0-------┑")
	print("|\t\t恐龙岛——萌龙大乱斗用户登录")
	print("|\t\t1.用户登录")
	print("|\t\t2.用户注册")
	print("|\t\t3.退出系统")
	print("┕-----------------------------------------------------------┙")
	
	choice=input("请输入你的选项：")
	if choice=="1":
		username=input("请输入你的账号： ").strip()
		password=input("请输入你的密码：").strip()
		for u in users:
			if u[0]==username and u[1]==password:
				input("登录成功,按任意键继续")

				while True:
					os.system("cls")
					
					print("-------------------------------------------------------")
					print("\t\t欢迎来到宠物家园")
					print(" ")
					print("\t1.查看领养的所有宠物")
					print("\t2.根据名称查询宠物是否已领养")
					print("\t3.捐赠一只宠物")
					print("\t4.修改宠物昵称")
					print("\t5.领养一只新宠物")
					print("\t6.退出系统")
					print(" ")
					print("-------------------------------------------------------")\
					
					choice=input("请输入你的选项：")
					if choice=="1":
						for pet in pets:
							print("已经领养的宠物：<%s>"%pet)
						else:
								input("查询完成。按任意键退出")
					elif choice=='2':
						name=input("请输入你要查询宠物的名称：")
						if name in pets:
							input("该宠物已经被领养")
						else:
							input("该宠物尚未领取，你可以带回家")
						input("查询完成，按任意键返回")
					elif choice=="3":
						name=input("请输入你要捐赠宠物的名称：")
						if name in pets:
							comfirm=input("您确定捐赠吗？Y/N？")
							if comfirm.lower()=="y":
								pets.remove(name)
							else:
								input("感谢您的捐赠,按任意键返回")
						else:
							input("该宠物尚未领养，不能捐赠，按任意键返回主菜单")
						

					elif choice=="4":
						name=input("请输入你要修改宠物的昵称：")
						index=pets.find(name)
						if index >=0:
							name=input("请输入新的昵称：")
							pets[index]=name
						else:
							print("该宠物尚未领养，麻烦请先领养")
						input("修改昵称操作结束。按任意键结束")

					elif choice=="5":
						name=input("请输入您要领养的宠物昵称")
						if name in pets:
							input("不好意思，您选定的宠物已经被领养，按任意键返回")
						else:
							pets.append(name)
							x=input("领养成功,按N键查看宠物特性，按任意键返回")
							if x=="N":
						#宠物详情
								while True:
									print("###################################################")
									print("#\t\t当前宠物亲密度：                     #"  )
									print("#\t\t当前宠物体力：                         #" )
									print("#\t\t1.安抚宠物                        #")
									print("#\t\t2.喂食宠物                        #")
									print("#\t\t3.一起玩耍                        #")
									print("#\t\t4.训练宠物                        #")
									print("#\t\t5.寻找战斗                        #")
									print("#\t\t6.返回上级                        #")
									print("#\t\t7.退出系统                        #")
									print("")
									choice=input("请输入你的选项：")
							else:
								print(" ")
					elif choice=="6":
						print("系统即将退出......")
						sys.exit(0)
					else:
						input("没有这个选项，按任意键继续")
	elif choice=="2":
		while True:
		
			username=input("请输入一个账号：").strip()
			password=input("请输入您的密码：").strip()
			passwordagin=input("请再次输入你的密码：").strip()
			if password==passwordagin:
				#定义一个空列表
				user=[]
				user.append(username)
				user.append(password)
				users.append(user)
				input("注册成功，按任意键返回主菜单")
				break
			else:
				input("两次输入不一致，按任意键继续")
				

	elif choice=="3":
		print("系统即将退出.....")
		sys.exit(0)

	else:
		input("没有这个选项，按任意键重新选择")

			
