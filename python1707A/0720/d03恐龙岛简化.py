"""
这是一个简易的恐龙岛系统
"""
#定义展示界面
def showmenu():
	print("这里是主界面")
	choice=input("")
	if choice=="1":
		login()
	elif choice=="2":
		regin()
	elif choice=="3":
		sys.exit(0)
	else:
		input("没有这个选项")
#定义登陆函数
def login():
	print("用户登录")
	input("登陆成功")
	showmenuwd()
def regin():
	print("注册成功")
	login()
def showmenuwd():
	input("这是系统界面")
showmenu()