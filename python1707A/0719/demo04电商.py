"""
利用函数的调用
写一个电商销售
包含计算器的运用
"""
#导入模块
import os,time,sys
#主界面函数
def mainwindow():
	print("=======================================")
	print("\t\t\t欢迎来到购物商城")
	print("\t\t1.购买商品")
	print("\t\t2.计算器")
	print("\t\t3.退出系统")
	print("=======================================")
#计算器函数
def caculation(num1,num2,opra):
	result=0
	if opra=="+":
		result=num1+num2
	elif opra=="-":
		result=num1-num2
	elif opra=="*":
		result=num1*num2

	return result
#二级页面
def windows():
	print("=======================================")
	print("\t\t1.商品 单价：999")
	print("=======================================")
while True:
	mainwindow()
	choice=input("请输入你的选项：")
	if choice=="1":
		windows()
		choice=input("请输入你要购买的商品：")
		num=int(input("请输入你要购买的数量"))
		pay=caculation(999,num, "*")
		
		
		print("您购买的总价为%s数量为%s" %(pay,num))
		money=int(input("请输入你的支付金额："))
		res=caculation(money,pay,"-")
		if res < 0:
			print("付款金额不足，返回继续操作.")
		else:
			input("购买成功，找零：%s； 按任意键返回主菜单" % res)
	elif choice=="2":
		num1=int(input("输入第一个："))
		opra=input("输入符号：")
		num2=int(input("输入第二个："))
	
		res=caculation(num1,num2,opra)
		input("结果为%s"% res)
		
	elif choice=="3":
		print("系统即将退出")
		time.sleep(2)
		sys.exit(0)
	else:
		input("没有这个选项，按任意键继续")
