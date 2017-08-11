'''
这是一个计算器  帮助你更好的计算数值等一系列操作

'''
#导入math模块
import math
right=True
#提醒用户输入第一个数值
num1=input("请输入第一个数值：")
num1=num1.strip()
#对输入的第一个数值进行判断
if num1.isdigit():
	num1=int(num1)
	opra=input("请输入你要运算的符号：")
	#对运算符误操作进行剔除
	opra=opra.strip()
	#定义变量
	result=0


	#对输入的运算符判断
	if opra=='sin':
		#将弧度转换为角度
		num1=math.radians(num1)
		result=math.sin(num1)
	elif opra=='cos':
#将弧度转换为角度
		num1=math.radians(num1)
		result=math.cos(num1)
	elif opra=='tan':
		#将弧度转换为角度
		num1=math.radians(num1)
		result=math.tan(num1)
	elif opra=='cot':
		#将弧度转换为角度
		num1=math.radians(num1)
		result=math.cot(num1)

	else:
		num2=input("请输入第二个数值：")
		#剔除空格
		num2=num2.strip()
		
		#对第二个数值判断
		if num2.isdigit():
			num2=int(num2)
			#对输入的运算符进行判断
			if opra=='+':
				result=num1+num2
			elif opra=='-':
				result=num1-num2
			elif opra=='*':
				result=num1*num2
			elif opra=='/':
				result=num1/num2
			else:
				right=False
				print("你的运算符输入错误了，系统退出！")
		else:
			#当第二次数值输入时错误
			right=False
			print("您输入的第二个数值有误，系统强制退出!！")



else:
#当用户输入的第一个数值错误时
	right=False
	print("您输入的第一个数值有误系统强制退出！!！")
if right:
	#当所有输入都合法时
	print("您的计算结果是：%s"% result)
