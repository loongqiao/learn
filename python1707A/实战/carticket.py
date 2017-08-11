"""
这是一个
车站卖票系统
可以处理紧急事件
"""
#导入sys模块
import sys
#打印界面
print("--------------------------------------------------------------------")
print("\t\tXX车站欢迎你")
print("   ")
print("\t\t1.开始购票")
print("\t\t2.退出系统")
print(" ")
print("--------------------------------------------------------------------")

while True:
	#用户进行选择
	choice=input("请输入你的选项：")
	
	if choice=="1":
		#定义一个变量
		ticket=100
	
	#开始售票

		while ticket>0:
			ticket -=1
			print("卖了%s张票，剩余%s张票"%((100-ticket),ticket))
			if ticket==10:
				it=input("城管来了，是否告警（是/否）?")
				if it=="是":
					print("提前下班")
					break
				else:
					print("继续卖票")
					continue
				
					
		else:
			print("票卖完了，下班回家")
		print("又是忙碌的一天啊")	
		
	elif choice=="2":
		print("系统即将退出.....")
		sys.exit(0)
	else:
		input("没有这个选项按任意键继续....")