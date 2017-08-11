"""
恐龙岛宠物大乱斗系统
1. 使用字典，改造恐龙岛
要求：用户信息使用字典(dict)保存
系统中所有的用户，使用列表保存
u1 = {...}
u2 = {...}
users = [u1, u2]
宠物使用字典保存
系统中所有的宠物，使用元组保存
p1 = {...}
p2 = {...}
pets = (p1, p2)
2. 实现功能
注册、登录
登录后界面的展示【领养宠物|宠物操作】
和宠物交互【爱抚|喂食|玩耍|战斗 完成1个即可】
"""
 #导入系统模块
import os,sys,time
#定义内测用户列表
u1=["admin","admin","葫芦娃",[]]
u2=["manger","123","奥特曼",[]]
users=[u1,u2]
while True:
	os.system("cls")
	#展示初级界面
	print("//////////////////////////////////////////////////////////////")
	print("//////////////////////////////////////////////////////////////")
	print("\t\t\t欢迎来到恐龙岛欢乐谷")
	print("\t\t\t1.用户登录")
	print("\t\t\t2.用户注册")
	print("\t\t\t3.退出系统")
	print("//////////////////////////////////////////////////////////////")
	print("//////////////////////////////////////////////////////////////")	
	choice=input("请输入你的选项：")
	if choice=="1":
		while True:
			userword=input("请输入你的账号：")
			password=input("请输入你的密码：")
			for u in users:
				if (userword==u[0])and (password==u[1]):
					input("登录成功")
			else:	
				input("账号密码不一致，按任意键继续")
				continue	
	elif choice=="2":
		while True:
			
			userword=input("请输入你的注册账户（按R键返回主菜单）：").strip()
			if userword.lower()=="r":
				break
			else:
				#判断账号是否已经存在
				for u in users:
					if userword==u[0]:
						input("您输入的账号已经被注册，按任意键继续注册")
						break
						
				else:
					password=input("请输入你的密码：").strip()
					passwords=input("请再次输入你的密码：").strip()
					nickname=input("请输入你的昵称").strip()
					#定义一个列表，用来存储注册的账号
					user=[]	
					if password==passwords:
						#将注册的信息存储在列表中
						user.append(userword)	
						user.append(password)
						user.append(nickname)
						users.append(user)
					input("注册完成按任意键返回主界面")
					break

	elif choice=="3":
		print("系统即将推出，有缘下次再见.....")
		#time.sleep(3)
		sys.exit(0)
	else:
		input("没有这个选项，按任意键继续")


