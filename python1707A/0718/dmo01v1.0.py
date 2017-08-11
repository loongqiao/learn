"""
恐龙岛-1.0版本
完成主要登陆界面展示
登录界面不同选项的定义
"""
#导入模块
import os
import sys
import time
#初始化内测账号
u1=["admin","123123","社会王"，[]]
u2=["manager","123456","阿王"，[]]
users=[u1,u2]
#初始
p1=["战斗暴龙兽","雄性","主人待定"，["龙卷雨击","龙啸九天"，"狂风绝息斩"]]
p2=["钢铁加鲁鲁","雄性","主人待定"，["刀光剑影","斩风绝"，"愤怒一击"]]
p3=["飞虫兽","雌性","主人待定"，["花仙炮","终极光线"，"能量倾泄"]]
pets=[p1,p2,p3]
while True:
	#展示界面
	print("/-----------------------------------------------/")
	print("/\t 大乱斗登录系统/")
	print("/\t1.用户登录/")
	print("/\t2.用户注册/")
	print("/\t3.退出系统/")
	print("/-----------------------------------------------/")
	choice=input("请输入你的选项：")
	if choice=="1":
		pass
	elif choice=="2":
		#用户输入账号
		while True:
			user=input("请输入注册账号,按R键返回：").strip()
			if username==R:

				break
			else:
				for u in users:
					if username==u[0]:
						input("该账号已经被注册,按任意键继续注册")
						break
				else:
					userpass=input("请输入登陆面膜")

		

	elif choice=="3":
		input("再见，希望下次光临")
		time.sleep(3)#系统在这停留三秒
		sys.exit(0)#系统退出
	else:
		input("没有这个选项，按任意键继续")