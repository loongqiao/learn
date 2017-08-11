"""
This is a dragon island game 
you can choice a pet as your pets
"""
#get a moudle
import os,sys,pickle,time
p1={"name":"cat","skill":"Grab","k":"5"}
p2={"name":"dog","skill":"Bite","k":"5"}
#the user data
users=[]
pets=(p1,p2)
loginuser={}
def reads():
	global users
	try:
		with open("users.dat","br") as f:
			users=pickle.load(f)
	except:
		users=[]
def write():
	with open("users.dat","bw")as f:
		pickle.dump(users,f)

#define a menu for  login and regist
def loginmenu():
	print(users)
	print("/////////////////////////////////////////////////////////////////////////")
	print("\t\tWelcome dragon island Game")
	print("\t\t1.login")
	print("\t\t2.regin")
	print("\t\t3.exit")
	print("/////////////////////////////////////////////////////////////////////////")
	choice=input("please enter your choice:")
	if choice=="1":
		login()
	elif choice=="2":
		regist()
	elif choice=="3":
		print("System exit at now")
		write()
		#time.sleep(3)
		sys.exit(0)
	else:
		input("Your choice error,please try agin")
		loginmenu()
#login
def login():
	username=input("Pleasee input your username:")
	password=input("Please input your password:")
	for u in users:
		if username==u.get("username")and u.get("password")==password:
			
			loginuser=u.copy()
			print(users)
			input("Contratulations!Successfully!")
			if loginuser.get("pet","no")=="no":
				showpets()
			else:
				showmainmenu()
			break
	else:
		x=input("Sorry,your username or password Error,inout Q to regist or you can try agin")
		if x.lower()=="q":
			regist()
		else:
			login()
#define regist
def regist():
	username=input("Please input username to regist for you:").strip()
	for u in users:
		if username==u.get("username"):
			input("Sorry,your userword isalready in system,But you can regist other username")
	else:
		password=input("Please input your Password:").strip()
		nickname=input("Please input your name:").strip()
		#define a blank dict
		user={}
		user["username"]=username
		user["password"]=password
		user["nickname"]=nickname
		users.append(user)
		input("Contratulations!Regist Successfully!")
		login()
#define showpets
def showpets():
	loginmenu()
	global loginuser
	#show pets
	print("//////////////////////////////////////////////////////////////")
	for p in pets:
		print("name:%s"%p.get("name"))
		print("skill:%s"%p.get("skill"))	
		print("=================================")
	print("//////////////////////////////////////////////////////////////")
	c=input("Please choice your pet:")
	for p in pets:
		if c==p.get("name"):
			loginuser["name"]=p
			for u in users:
				if loginuser.get("username")==u.get("username"):
					u["pet"]=p
					showmainmenu()
#defin showmainmenu
def showmainmenu():
	print("name:%s"%loginuser.get("nickname"))
	print("pet's name:%s"%loginuser["pet"]["name"])
	print("pet's skill:%s"%loginuser["pet"]["skill"])
	print("pet's qmd:%s"%loginuser["pet"]["k"])
	input("sdsd")

reads()					
#come in begin
loginmenu()