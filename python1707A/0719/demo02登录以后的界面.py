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
"ins":"你皮任你皮"
登录后界面的展示【领养宠物|宠物操作】
和宠物交互【爱抚|喂食|玩耍|战斗 完成1个即可】
"""
 #导入系统模块
import os,sys,time
#定义内测用户列表
u1={"userword":"admin","password":"123456","nickname":"huluwa","pet": {"name":"皮皮虾","sex":"雄性", "zhuren":"亚索","skill":"狂风暴雨", "qmd": 2,"ins":"你皮任你皮"}}
u2={"userword":"manger","password":"123321","nickname":"aotaman","pet":{}}
users=[u1,u2]
loginuser={}
p1 = {"name":"皮皮虾","sex": "雄性","zhuren": "主人待定","skill":"狂风暴雨", "qmd":2, "ins":"你皮任你皮"}
p2 = {"name":"象拔蚌", "sex":"雌性", "zhuren":"主人待定", "skill":"猛龙摆尾","qmd":2, "ins":"我有冬瓜皮"}
p3 = {"name":"灵灵狗", "sex":"雄性", "zhuren":"主人待定", "skill":"杀人不留血","qmd": 2,"ins":"我有西瓜皮"}
pets=(p1,p2,p3)
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
				if (userword==u["userword"])and (password==u["password"]):
					loginuser=u.copy()
					input("登录成功")
					break
			else:	
				input("账号密码不一致，按任意键继续")
				continue
			#展示领养宠物界面
			while len(loginuser["pet"])<=0:
				print("=============================================================")
				print("\t\t\t恐龙岛欢乐谷宠物信息")
				for u in pets:
					print("\t名称：%s，性别：%s，主人：%s"%(u["name"],u["sex"],u["zhuren"]))
					print("\t技能：%s"%u["skill"])
					print("\t亲密度：%s ,介绍：%s"%(u["qmd"],u["ins"]))
					print("___________________________________________________________________________________________")
				print("=============================================================")	
				name=input("请输入你选择的宠物：")
				for pet in pets:
					pet[""]


			#展示宠物信息
			if loginuser.get("pet","no")!="no":
				print("=============================================================")
				print("\t名称：%s，性别：%s，主人：%s"%(loginuser["pet"]["name"],loginuser["pet"]["sex"],loginuser["pet"]["zhuren"]))
				print("\t技能：%s"%loginuser["pet"]["skill"])
				print("\t亲密度：%s ,介绍：%s"%(loginuser["pet"]["qmd"],loginuser["pet"]["ins"]))
				print("___________________________________________________________________________________________")
				print("=============================================================")	
	elif choice=="2":
		while True:
			
			userword=input("请输入你的注册账户（按R键返回主菜单）：").strip()
			if userword.lower()=="r":
				break
			else:
				#判断账号是否已经存在
				for u in users:
					if userword==u["userword"]:
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
						user={}
						user["userword"]=userword	
						user["password"]=password
						user["nickname"]=nickname
						pet={}
						user["pet"]=pet
						users.append(user)
					input("注册完成按任意键返回主界面")
					break

	elif choice=="3":
		print("系统即将推出，有缘下次再见.....")
		#time.sleep(3)
		sys.exit(0)
	else:
		input("没有这个选项，按任意键继续")
		


