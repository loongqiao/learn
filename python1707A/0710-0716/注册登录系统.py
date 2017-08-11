"""
一个简单的子系统 
用于英雄联盟商城
账号密码的注册以及登录
"""
#引入sys模块
import sys
#打印用户界面
print("----------------------------------------------------------")
print("\t\t\t欢迎来到召唤师峡谷商店")
print("\t\t1.登录英雄商城")
print("\t\t2.商城账号的注册")
print("\t\t3.退出系统")
print("----------------------------------------------------------")
#定义一个空列表用来储存账号密码
users=[]

while True:
	
	while True:
		choice=input("请输入你的选项：")
		if choice=='1':
			username=input("请输入你的账号：").strip()
			password=input("请输入你的密码：").strip()
			for u in users:
				if u[0] == username and u[1] == password:
					input("登陆成功，按任意键继续")
					break 
				else:
					input("您输入的账号密码不一致")
					continue
		elif choice=='2':
			#输入账号密码
			username=input("请输入你的账号：").strip()
			password=input("请输入你的密码：").strip()
			passwords=input("请再次输入你的密码：").strip()	
			if password==passwords :
				user=[]
				
				#将数据存在列表中
				user.append(username)
				user.append(password)
				users.append(user)
				print("注册完成")
				input("按任意键返回主菜单....")
				break


			else:
				input("两次输入不一致，按任意键继续....")
			#系统退出操作
		elif choice=='3':
			print("系统即将退出.....")
			sys.exit(0)
		else:
			print("您输入的有误,请重新输入")
			continue



