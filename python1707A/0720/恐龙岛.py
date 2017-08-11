"""
恐龙岛案例and 字典
"""
u1={"username":"admin","password":"admin","nickname":"哈撒K","pet":{"name":"黄金兽","skill":["浩然正气","蛟龙出海"]}}
u2={"username":"123456","password":"123456","nickname":"面对疾风"}
users=[u1,u2]
p1={"name":"黄金兽","skill":["浩然正气","蛟龙出海"]}
p2={"name":"泥石怪","skill":["借力还力","祝融取火"]}
p3={"name":"冰雪魔","skill":["天魔解体","袖里乾坤"]}
pets=[p1,p2,p3]
loginuser={}
import sys,os,time
while True:
	print("==================================================")
	print("\t\t欢迎来到恐龙岛")
	print("\t1.用户登录")
	print("\t2.用户注册")
	print("\t3.退出系统")
	print("==================================================")
	choice=input("请输入你的选项：")
	if choice=="1":
		username=input("请输入泥的账号")
		password=input("请输入你的密码")
		for u in users:
			if (username==u.get("username"))and (password==u.get("password")):
				
				loginuser=u.copy()
				input("登陆成功")
				break
		else:
			input("账号密码错误")
			continue
		while loginuser.get("pet","no")=="no":
			print("=====================================")
			for p in pets:
				print("名称：%s"%p.get("name"))
				print("技能：%s"%p.get("skill"))
				print("------------------------------------------")
			print("=====================================")
			c=input("请输入你的选择：")
			for p in pets:
				if c==p.get("name"):
					loginuser["pet"]=p
					for user in users:
						if loginuser.get("username")==user.get("username"):
							user["pet"]=p
							print(users)








	elif choice=="2":
		username=input("请输入你的注册账号：")
		password=input("请输入你的密码：")
		nickname=input("请输入你的昵称：")
		user={}
		user["username"]=username
		user["password"]=password
		user["nickname"]=nickname
		users.append(user)
