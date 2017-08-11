"""
恐龙岛 宠物大乱斗
1.0版本
实现用户的注册登录功能
"""
#导入系列模块
import os
import sys
import time
#系统预留的内测账号密码
u1=["admin","admin","疾风剑豪",["皮皮虾", "雄性", "张小凡", ["狂风暴雨", "龙卷雨击", "龙啸九天"], 2, "你皮任你皮"]]
u2=["manger","123","暴走萝莉",[]]
users=[u1,u2]
# 定义一个变量，用来当前登录的用户
loginuser = []
#初始化三个宠物
# 初始化3个宠物
p1 = ["皮皮虾", "雄性", "主人待定", ["狂风暴雨", "龙卷雨击", "龙啸九天"], 2, "你皮任你皮"]
p2 = ["象拔蚌", "雌性", "主人待定", ["猛龙摆尾", "亢龙有悔", "飞龙在天"], 2, "我有冬瓜皮"]
p3 = ["灵灵狗", "雄性", "主人待定", ["杀人不留血", "十步杀一人", "千里不留行"], 2, "我有西瓜皮"]
pets=[p1,p2,p3]

while True:
	#清屏
	os.system("cls")
	#展示登陆页面
	print("/-----------------------------------------------------------")
	print("/\t\t欢迎来到恐龙岛--大乱斗")
	print("/\t\t1.用户登录")
	print("/\t\t2.用户注册")
	print("/\t\t3.退出系统")
	#用户选择
	choice=input("请输入你的选项：")
	#用户登录
	if choice=="1":
		
		username=input("请输入你的账号：")
		password=input("请输入你的密码：")
		for u in users:
			if username==u[0] and password==u[1]:
				loginuser=u.copy()

				input("nihao")
				break
		else:
			input("账号密码不一致，请重新输入")
			continue
		while len(loginuser[3])<=0:      #没有领养宠物
			#展示领养宠物界面
			os.system("cls") 
			print("\t\t恐龙岛宠物展示界面")
			print("------------------------------------------------")
			for p in pets:
				print("\t名称：%s，性别：%s，主人：%s"%(p[0],p[1],p[2]))
				print("\t技能：%s"%p[3])
				print("\t亲密度：%s ,台词：%s"%(p[4],p[5]))
				print("____________________________________________")
			print("-------------------------------------------------")
			name=input("请选的你要领养的宠物：")
			for pet in pets:
				#判断用户输入是否正确
				if pet[0]==name:
					#将宠物的名称添加到临时账户中并赋值到相应的位置
					pet[2]=loginuser[2]
					loginuser[3]=pet.copy()

					#更新用户列表
					for u in users:
						if (u[0]==loginuser[0]) \
						and (u[1]==loginuser[1]):
							index=users.index(u)
							u[3]=pet.copy()
							users[index]=u
					input("领养成功，按任意键继续")
					break	

			else:
				input("您输入的宠物有误，请重新输入")
				continue
		while len(loginuser[3])>0:
			os.system("cls")

			print("-------------------------------------------")
			print("宠物名字：%s \t\t|"%loginuser[3][0])
			print("宠物性别：%s\t\t|"%loginuser[3][1])
			print("宠物主人：%s\t\t|"%loginuser[3][2])
			print("宠物技能：%s\t\t|"%loginuser[3][3])
			print("宠物亲密度：%s\t\t|"%loginuser[3][4])
			print("宠物台词：%s\t\t|"%loginuser[3][5])
			print("-------------------------------------------")
			print("\t\t1.摸摸哒")
			print("\t\t2.加个餐")
			print("\t\t3.跑3000")
			print("\t\t4.玩耍")
			print("\t\t5.战斗")
			print("\t\t6.返回主菜单")
			print("-------------------------------------------")
			choice=input("请输入你的选项：")
			if choice=="1":
				print("哈哈哈哈哈哈哈。。。")
				print("呸，贼讨厌")
				time.sleep(2)
				k=loginuser[3][4]
				k+=1
				loginuser[3][4]=k
				#更新用户列表
				for u in users:
					if (u[0]==loginuser[0]) \
					and (u[1]==loginuser[1]):
						index=users.index(u)
						
						users[index]=u
				input("摸摸哒结束")
			elif choice=="2":
				print("吃食了！！！")
				print("我就喜欢吃吃吃！！")
				time.sleep(2)
				k=loginuser[3][4]
				k+=1
				loginuser[3][4]=k
				#更新 用户列表
				for u in users:
					if (u[0]==loginuser[0]) \
					and (u[1]==loginuser[1]):
						index=users.index(u)
						
						users[index]=u
				input("吃食结束")
			

			elif choice=="3":
				print("跑步了")
				print("跑个毛线")
				time.sleep(2)
				k=loginuser[3][4]
				k-=1
				loginuser[3][4]=k
				for u in users:
					if (u[0]==loginuser[0]) \
					and (u[1]==loginuser[1]):
						index=users.index(u)
						
						users[index]=u
				input("跑步结束")
			

			elif choice=="4":
				
				print('"石头剪刀布 ,布"')
				
				time.sleep(2)
				print('"石头剪刀布 ,石头"')
				k=loginuser[3][4]
				k+=1
				loginuser[3][4]=k
				for u in users:
					if (u[0]==loginuser[0]) \
					and (u[1]==loginuser[1]):
						index=users.index(u)
						
						users[index]=u
				input("玩耍结束")
				
			elif choice=="5":
				print('"站个痛快"')
				
				time.sleep(2)
				print('"来吧"')
				k=loginuser[3][4]
				k-=1
				loginuser[3][4]=k
				for u in users:
					if (u[0]==loginuser[0]) \
					and (u[1]==loginuser[1]):
						index=users.index(u)
						
						users[index]=u
				
			elif choice=="6":
				break
			else:
				input("没有这个选项")

			
#用户注册
	elif choice=="2":
		while True:
			username=input("请输入你的选项：输入你要注册的账号,按R键返回主菜单：").strip()
			if username.lower()=="r":
				break
			else:
				for u in users:
					if username==u[0]:
						input("您输入的账号已被注册,按任意键继续注册:")
						break
						
				else:
					password=input("请输入你的登陆密码：").strip()
					passwords=input("请再次输入你的登录密码：").strip()
					nickname=input("请输入昵称：").strip()					
					#创建一个空列表，用来存储注册的信息
					user=[]
					if password==passwords:
						user.append(username)
						user.append(password)
						user.append(nickname)
						user.append(list([]))
						users.append(user)
						input("注册完成，按任意键返回")
						break
					else:
						input("两次输入不一致，请重新输入")




			
		



	elif choice=="3":
		print("系统即将退出，下次再见。")
		time.sleep(3)#程序停留三秒
		sys.exit(0)

	else:
		input("没有这个选项，按任意键继续")

