#界面介绍
import os 
import math
os.system("cls")
print("\t\t\t欢迎使用计算器")
print("************************************************************************************************")
print("*             1              2            3                 +                                  *")
print("*                                                                                              *")
print("*                                                                                              *")
print("*             4              5            6                  -                                 *")
print("*                                                                                              *")
print("*             7              8            9                 *                                  *")
print("*                                                                                              *")
print("*              %            0            ^                 /                                   *")
print("*                                                                                              *")
print("*             sin          cos          tan               cot                                  *")
print("************************************************************************************************")

#运算详情
x=input("请输入第一个数字： ")
x.isdigit()
if x.isdigit():
	opration=input("请输入要进行的运算+ - * / ^ %:")
	y=input("请输入第二个数字: ")
	x=int(x)
	y=int(y)

	#运算判断
	if opration== "+":
		z=x+y
		print("您所运算的结果是： "+str(z))
	elif opration=="-":
		z=x-y
		print("您所运算的结果是： "+str(z))
	elif opration=="*":
		z=x*y
		print("您所运算的结果是： "+str(z))
	elif opration=="/":
		z=x/y
		print("您所运算的结果是： "+str(z))
	elif opration=="^":
		z=x**y
		print("您所运算的结果是： "+str(z))
	elif opration=="%":
		z=x%y
		print("您所运算的结果是： "+str(z))
else:
	if x=='sin':
	            y=int(input("请输入数值： "))
	            z=math.sin(y)
	            print("sin %s=%s:"% (str(y),z))
	elif x=='cos':
		y=int(input("请输入数值： "))
		z=math.cos(y)
		print("cos %s=%s:"% (str(y),z))
	elif x=='cos':
		y=int(input("请输入数值： "))
		z=math.cos(y)
		print("cos %s=%s:"% (str(y),z))	            
	elif x=='tan':
		y=int(input("请输入数值： "))
		z=math.tan(y)
		print("tan %s=%s:"% (str(y),z))
	elif x=='cot':
		y=int(input("请输入数值： "))
		z=math.cos(y)
		print("cot %s=%s:"% (str(y),z))
	else:
		print('您的输入有误系统强制退出！')            	            