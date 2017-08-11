"""
恐龙岛-1.0版本
完成主要登陆界面展示
登录界面不同选项的定义
"""
#导入模块
import os
import sys
import time
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

		pass

	elif choice=="3":
		input("再见，希望下次光临")
		time.sleep(3)
		sys.exit(0)
	else:
		input("没有这个选项，按任意键继续")