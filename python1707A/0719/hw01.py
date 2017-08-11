"""
新闻管理系统：项目名称（news.py）
	查看所有新闻
	查看某条新闻
	发布一条新闻
	删除一条新闻
	修改新闻内容

技术要求1：数据存储的情况
新闻列表：列表list
新闻：字典dict
新闻数据{新闻标题、发布时间、记者姓名、新闻内容}
技术要求2：函数封装
	查看、发布、删除、修改全部封装成函数
"""
#定义两个内测账号
u1={"userword":"admin","password":"123456"}
u2={"userword":"manger","password":"123321"}
users=[u1,u2]
w1={"地点":"郑州","天气":"晴","日期":"20","温度":"35C-40C",}
w2={"地点":"上海","天气":"阴","日期":"20","温度":"36C-41C"}
w3={"地点":"北京","天气":"晴","日期":"21","温度":"38C-45C"}
weas=[w1,w2,w3]

def show1():
	print("//////////////////////////////////////////////////////////////////")
	print("\t\t\t欢迎光临天气预报网")
	print("\t\t1.用户登录")
	print("\t\t2.用户注册")
	print("\t\t3.退出系统")
def showmain():
	print("//////////////////////////////////////////////////////////////////")
	print("\t\t\t欢迎光临天气预报")
	print("\t\t\t1.查看所有地点的天气预报")
	print("\t\t\t2.查看某地的天气预报")
	print("\t\t\t3.发布一条天气预报")
	print("\t\t\t4.删除一条天气预报")
	print("\t\t\t5.修改天气预报")
	print("\t\t\t6.返回上一级")
	print("//////////////////////////////////////////////////////////////////")

def zhuce(username,password):
	user=[]
	if password==passwords:
		#将注册的信息存储在列表中
		user={}
		user["userword"]=userword	
		user["password"]=password
		users.append(user)
#定义一个可以遍历的函数
def check1():
	for u in weas:
		print("======================================")
		print("地点： %s"%u["地点"])
		print("天气： %s"%u["天气"])
		print("日期： %s"%u["日期"])
		print("温度： %s"%u["温度"])
		"""for u in weas:
			print("======================================")
			print("地点： %s"%u.get("地点"))
			print("天气： %s"%u.get("天气"))
			print("日期： %s"%u.get("日期"))
			print("温度： %s"%u.get("温度"))"""
#查询某天的天气
def check2(pl):
	for wea in weas:
		if pl==wea["地点"]:
			
			print("地点：%s,天气:%s,日期:%s,温度：%s"%(wea["地点"],wea["天气"],wea["日期"],wea["温度"]))
##if pl==wea.get("地点"):
	#print("地点：%s,天气:%s,日期:%s,温度：%s"%(wea.get("地点"),wea.get("天气"),wea.get("日期"),wea.get("温度"))
	
#新增一条天气
def check3():
	wea4={}
	place=input("请输入地点")
	weather=input("天气：")
	date=input("日期：")
	tm=input("温度")
	wea4["地点"]=place#	wea4.get("地点")=place
	wea4["天气"]=weather	#wea4.get("天气")=weather
	wea4["日期"]=date	#wea4.get("日期")=date
	wea4["温度"]=tm	#wea4.get("温度")=tm
	weas.append(wea4)
#删
def check4():
	place=input("请输入你要删除的地点：")
	for wea in weas:
		
		if place==wea["地点"]:
			weas.remove(wea)
#改
def check5():
	place=input("请输入你要修改的地点：")
	for wea in weas:
		if place==wea["地点"]:	#if place==wea.get("地点")

			pp=input("请输入新地点：")
			wea["地点"]=pp
#wea.get("地点")=pp				
while True:
	show1()
	choice=input("请输入你的选项：")
	if choice=="1":
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
		while True:
			showmain()
			choice=input("请输入你的选项：")
			if choice=="1":
				check1()
				input("按任意键返回")
			elif choice=="2":
				pl=input("请输入你要查看的地点")
				check2(pl)
				input("按任意键返回")
			elif choice=="3":
				check3()
				
				input("按任意键返回")
			elif choice=="4":
				check4()
				
				input("按任意键返回")
			elif choice=="5":
				check5()
				
				input("按任意键返回")
			elif choice=="6":
				
				input("按任意键返回")
				break





			
	#账号注册
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
					zhuce(userword,password)
					input("注册成功,按任意键返回")
					break
		

				