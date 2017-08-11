"""
这是一个私有字典的 
有用户的固定信息
可以增加信息
可以修改信息
可以查询信息
"""
users=[]
u1={"name":"a","age":"20","sex":"男","phone":"123456"}
u2={"name":"b","age":"18","sex":"女","phone":"124563"}
users.append(u1)
users.append(u2)

while True:

#打印界面
	print("\t\t信息查询")
	print("------------------------------------------------------------------")
	print("\t1.查看所有用户信息")
	print("\t2.客户信息修改")
	print("\t3.新增一个客户")
	print("\t4.客户资料查询")
	print("\t5.退出系统")
	print("------------------------------------------------------------------")
	choice=input("请输入你的选项：")
	if choice=="1": #遍历所有用户 
		for user in users:
			print("用户姓名:%s;年龄:%s;性别:%s，电话：%s" % (user.get("name"), \
					user.get("age"),user.get("sex"),user.get("phone")))
		else:
			input("按任意键返回上一层")
	elif choice=="2": #改

		
	elif choice=="3": #增加用户
		#定义一个空字典
	
		name=input("请请输入你要添加的姓名：").strip()
		age=input("请输入你要添加的年龄：").strip()
		xb=input("请输入你要添加的性别：").strip()
		pn=input("请输入电话号码").strip()
		#创建用户字典
		user={"name":name,"age":age,"sex":xb,"phone":pn}
		#存储信息
		users.append(user)
		input("用户添加完成，按任意键继续")


