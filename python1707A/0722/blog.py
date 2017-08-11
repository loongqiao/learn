"""功能
	用户登录
	用户注册
	查看所有博文
	查看自己发布的文章
	根据标题查看某一篇文章
	发表文章
	删除文章
	修改文章内容

分析数据：
	用户数据[users.dat]
		所有的用户，保存在一个列表中。 users
		用户属性：
			账号 username
			密码 password
			昵称 nickname
			性别 sex
			年龄 age
			联系方式 phone
			邮箱 email
			地址 address
	文章数据[articles.dat]
		所有的文章，保存在一个列表中. articles
		文章属性： article
			文章标题	title
			发布时间[参考datetime模块]	publish
			作者	author
			文章内容 content
分析功能：
	用户注册功能：
		要求：如果一个账号已经注册，不能使用重复的账号进行注册
			账号长度，必须是8~12位之间，账号必须全部是字母
			密码长度，必须是8~16位之间
	用户登录功能：
		用户必须输入账号+密码才能进行登录
			否则，提示用户输入账号密码
			[您的账号或者密码没有输入，请检查重新输入]
	主界面：
		[展示欢迎信息：尊敬的用户<昵称>您好，欢迎登陆个人博客系统]
		[可选：展示用户登录系统的时间]
		查看所有文章
		查看自己发布的文章
		发表文章
		删除文章
		修改文章
	查看所有文章：
		查看系统中所有账号发布的所有文章
		> 输入标题查看文章详细内容：
	查看个人文章：
		查看系统中自己发布过的所有文章
		> 输入标题查看文章详细内容：
	发表文章：
		输入标题：要求标题不能和任何文章的标题相同
		输入内容
		发布文章
	删除文章：
		查看自己发布过的所有文章，输入标题进行删除
		要求：不能删除别人发布的文章，会提示~该文章不是你发布的，您没有权限删除
	修改文章：
		输入文章标题【不能修改别人的文章】
		输入修改后的文章内容
		发布修改
"""
#导入模块
import time,sys,os,pickle,datetime
#定义一个列表用来存储所有的账号信息
users=[]
#定义一个列表用来存储所有文章信息】
arts=[]
#定义一个空字典存储临时用户
loginuser={}

#定义一个函数,现实登录界面
def loginMenu():
	
	os.system("cls")
	print(users)
	print("///////////////////////////////////////////////////////////////////")
	print("\t\t欢迎来到博客")
	print("\t\t1.用户登录")
	print("\t\t2.用户注册")
	print("\t\t3.退出系统")
	print("///////////////////////////////////////////////////////////////////")

	choice=input("请输入你的选项：")
	if choice=="1":
		login()
		
	elif choice=="2":
		regist()
	
	elif choice=="3":
		print("系统即将推出。")
		write()
		sys.exit(0)
	else:
		input("没有这个选项，按任意键继续")
		loginMenu()
#注册系统
def regist():
	username=input("请输入你的注册账号：").strip()
#判断账号是否全为字母
	res=username.isalpha()
#判断账号位数
	if (res==True)and(12>=len(username)>=8):

		for u in users:
			if username==u.get("username"):
				input("您输入的账号已经存在，请重新注册")
				regist()
		else:
			password=input("请输入你的密码（8-12）位")
			if (12>=len(password)>=8):
				#定义一个空字典
				user={}
				nickname=input("请输入你的昵称").strip()
				sex=input("请输入你的性别").strip()
				age=input("请输入你的年龄").strip()
				phone=input("请输入你的电话").strip()
				email=input("请输入你的邮箱").strip()
				address=input("请输入你的地址").strip()
				user["username"]=username
				user["password"]=password
				user["nickname"]=nickname
				user["sex"]=sex
				user["age"]=age
				user["phone"]=phone
				user["email"]=email
				user["address"]=address
				users.append(user)
				input("注册完成，按任意键回主页面")
				loginMenu()


			else:
				input("密码不合法请重新注册")
				regist()

	else:
		input("您输入的账号不符合规定")
		regist()
#登录函数
def login():
	global loginuser
	username=input("请输入账号")
	password=input("请输入密码")
	for u in users:
		if (u.get("username")==username)and(u.get("password")==password):
			input("登录成功")
			loginuser=u.copy()
			#print(loginuser)
			#input("dasdasda")
			showmainMenu()
	else:
		x=input("账号密码不一致，但是你可以按Q键前往注册，或者按任意键继续输入")
		if x.lower()=="q":
			regist()
		else:
			login()
#展示主页面			
def showmainMenu():
	os.system("cls")
	print("//////////////////////////////////////////////////////////////////////////////")
	print("\t\t\t欢迎来到博客网")
	print("\t\t\t\t\t日期：%s"%datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S")) #系统时间函数
	print("\t\t1.查看所有博文")
	print("\t\t2.查看自己发布的博文")
	print("\t\t3.根据标题查看某一篇文章")
	print("\t\t4.发表文章")
	print("\t\t5.删除文章")
	print("\t\t6.修改文章")
	print("\t\t7.返回主页面")
	c=input("输入你的选择：")
	if c=="1":
		All()
	elif c=="2":
		exclusive()
	elif c=="3":
		someTitle()
		

	elif c=="4":
		addArticle()
	elif c=="5":
		delart()
	elif c=="6":
		newcontent()
	elif c=="7":
		write1()
		loginMenu()
	else:
		showmainMenu()
#定义查看所有博文的函数
def All():
	os.system("cls")
	print("///////////////////////////////////////////////////////////")
	print("\t\t\t所有文章如下")
	for p in arts:
		print("标题：%s"%p.get("title"))
		print("内容：%s"%p.get("content"))
		print("作者：%s"%p.get("author"))
		print("发布日期%s"%p.get("date"))
		print("--------------------------------------------------")
	print("/////////////////////////////////////////////////////////////")
	input("按任意键返回主菜单")
	showmainMenu()
#定义一个函数用来查看自己发布的文章
def exclusive():#exclusive 专属
	for u in arts:
		if u.get("author")==loginuser.get("nickname"):
			print(u)
			input("按任意键继续")
			showmainMenu()
#根据标题查看文章
def someTitle():
	t=input("请输入查看的标题")
	for a in arts:
		if a.get("title")==t:
			print("内容如下：%s"%a.get("content"))
			input("按任意键返回主菜单")
			showmainMenu()
	else:
		input("您查找的文章不存在，按任意键重新输入")
		someTitle()
#新增文章
def addArticle():
	global loginuser
	title=input("请输入标题")
	for a in arts:
		if a.get("title")==title:
			input("您输入的标题已经存在，按任意键重新输入")
			addArticle()
	else:
		content=input("请输入内容")
		
		#创建一个字典存贮文章
		art={}
		art["title"]=title
		art["content"]=content
		art["author"]=loginuser["nickname"]
		art["date"]=datetime.datetime.now().strftime(" %Y-%m-%d %H:%M:%S")
		arts.append(art)
		print(art)
		#l=loginuser["nickname"]
		#print(l)
		input("添加成功，按任意键回主菜单")
		showmainMenu()
#删除文章
def delart():
	title=input("请输入你要删除的标题")
	for u in arts:
		if u.get("title")==title:
			arts.remove(u)
			input("删除成功，按任意键回主菜单")
			showmainMenu()
#修改文章
def newcontent():
	title=input("请输入你要更改文章的标题")
	for u in arts:
		if (u.get("title")==title)and(u.get("author")==loginuser.get("nickname")):
			xx=input("请输入新的内容")
			u["content"]=xx
			input("修改成功，按任意键回主菜单")
			showmainMenu()







def read1():
	global arts
	try:
		with open("arts.dat","br")as f:
			arts=pickle.load(f)
	except:
		arts=[]


def read():
	global users
	try:
		with open("users.dat","br")as f:
			users=pickle.load(f)
	except:
		users=[]
def write():
	with open("users.dat","bw")as f:
		pickle.dump(users,f)
def write1():
	with open("arts.dat","bw")as f:
		pickle.dump(arts,f)
read()
read1()
#程序的入口
loginMenu()


