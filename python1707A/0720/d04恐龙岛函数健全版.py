"""
恐龙岛II
利用函数反复调用
实现界面跳转
已经登录注册等
"""
#导入模块
import os,sys,time
#定义两个内测用户
u1={"username":"admin","password":"admin","nickname":"夜灵溪","pet":{"name":"黄金兽","skill":["浩然正气","蛟龙出海","鸣烟销骨"],"k":"5"}}
u2={"username":"qwe","password":"123456","nickname":"幽梦影"}
#定义一个空字典将U1U2添加进去
users=[u1,u2]
#定义宠物
p1={"name":"黄金兽","skill":["浩然正气","蛟龙出海","鸣烟销骨"],"k":"5"}
p2={"name":"泥石怪","skill":["借力还力","祝融取火","雷神怒击"],"k":"5"}
p3={"name":"冰雪魔","skill":["天魔解体","袖里乾坤","嗤骨抽髓"],"k":"5"}
#定义一个元组
pets=(p1,p2,p3)
#定义一个空字典，用来存储临时数据
loginuser={}

#开始页面
def showbg():
	print("====================================")
	print("\t\t欢迎来到恐龙岛II")
	print("\t\t1.用户登录")
	print("\t\t2.用户注册")
	print("\t\t3.退出系统")
	print("====================================")
	#用户进行算账
	choice=input("请输入你的选项：")
	if choice=="1":
		login()
		

	elif choice=="2":
		res=regin()
		if res==True:
			input("注册结束，按任意键进入账号登录\n\n")
			login()
	

	elif choice=="3":
		print("系统即将推出")
		time.sleep(3) #系统在这里停留三秒
		sys.exit(0)

	else:
		input("输入有误，按任意键重新选择")
		showbg()
#定义注册函数
def regin():
	#引入全局变量
	global loginuser,pets,users
	username=input("请输入你要注册的账号：")
	for user in users:
		if user.get("username")==username:
			input("您输入的账号已经存在，按任意键继续注册").strip()
		else:
			password=input("请输入注册密码：").strip()
			passwords=input("请再次输入泥的密码：").strip()
			nickname=input("请输入你的昵称").strip()
			#判断两次输入密码是否一致
			if password==passwords:
				#定义一个空字典
				user={}
				user["username"]=username
				user["password"]=password
				user["nickname"]=nickname
				users.append(user)
				input("Congratulations,Register successfully!")
				return True
				login()
			'''login()
			else:
				input("两次输入不一致，按任意键继续注册")
				regin()'''

#登陆函数				
def login():
	#引入全局变量
	global loginuser,pets,users
	username=input("请输入你的账号：")
	password=input("请输入你的密码：")
	for user in users:
		if (user.get("username")==username)and(user.get("password")==password):
			loginuser=user.copy()
			input("登录成功，按任意键继续")
			print(user)
			#判断宠物是否有宠物
			if loginuser.get("pet","no")=="no":

				givepet()
			else:
				showpets()
			return True
	else:
		y=input("账号密码不一致，按Q键注册，按任意键重新输入账号密码：")
		if y.lower()=="q":
			res=regin()
			if res==True:
				login()
		return False
#宠物领养界面
def givepet():
	#引入全局变量
	global loginuser,pets,users
	print("===============================")
	for p in pets:
		print("名称：%s"%p.get("name"))
		print("技能：%s"%p.get("skill"))
		print("亲密度：%s"%p.get("k"))
		print("------------------------------------------")
	print("=====================================")
	print(loginuser)
	pet=input("请输入你想要的宠物：")

	for p in pets:
		if pet==p.get("name"):
			loginuser["name"]=p
			for u in users:
				if loginuser.get("username")==u.get("username"):
					u["pet"]=p
					showpets()

				
					
#宠物交互界面
def showpets():
	#引入全局变量
	global loginuser,pets,users
	print("//////////////////////////////////////////////////////////////////////")
	print("\t名字：%s"%(loginuser["pet"]["name"]))
	print("\t技能: %s"%(loginuser["pet"]["skill"]))
	print("\t亲密度：%s"%(loginuser["pet"]["k"]))
	print("----------------------------------------------------------------------")
	print("\t1.爱抚宠物") #aifu
	print("\t2.给宠物喂食")#el
	print("\t3.陪宠物玩耍")#pl
	print("\t4.训练宠物")#fl
	print("\t5.出击")#gl
	print("\t6.返回登录菜单")
	choice=input("请输入你的选项：")
	if choice=="1":
		aifu()
		pass
	elif choice=="2":
		weishi()
		pass
	elif choice=="3":
		wanshua()
		pass
	elif choice=="4":
		xunlian()
		pass
	elif choice=="5":
		chuji()
		pass
	elif choice=="6":
		showbg()








#程序入口
showbg()