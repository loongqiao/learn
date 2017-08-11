
"""
科学计算器
可以进行基本的运算也可以进行高级运算
"""
#导入math模块
import math
#导入sys模块
import sys
#导入os模块
import os
#打印界面
#定义列表用来存储计算符号
opra1=["+","-","*","/","//","**"]
opra2=["sin","cos","tan","cot"]
#定义一个空列表用来存放历史纪录
users=[]
while True:
	os.system("cls")
#主菜单
	user=[]
	print("\t\t  欢迎使用科学计算器")
	print("\t\t1.进入计算器")
	print("\t\t2.退出计算器")
	option=input("请输入你的选项：")

	
	if option=='1':
	#数据操作页面
		
		print("----------------------------------------------------------------")
		print(" ")
		print("\t9         8             7            +       sin                                     ")
		print(" ")
		print("\t6         5             4            -        cos                                    ")
		print(" ")
		print("\t3         2             1            *        tan                                     ")
		print(" ")
		print("\t**        0             //           /         cot                                     ")
		print(" ")
		print("----------------------------------------------------------------")
		while True:
			#用户输入第一个数值
			num1=int(input("请输入第一个你要计算的数值："))
			
			#用户输入运算符号
			opration=input("请输入你要运算的符号：")
			
			#定义一个参数，用来存储计算结果
			result=0
			#对输入的运算符号进行判断
			if (opration in opra2)or(opration in opra1):
				#当运算符号位于科学运算时
				if opration in opra2:
					if opration=="sin":
						result=math.sin(math.radians(num1))
					elif opration=='cos':
						result=math.cos(math.radians(num1))
					elif opration=='tan':
						result=math.tan(math.radians(num1))
					elif opration=='cot':
						result=math.cot(math.radians(num1))
				#当运算位于科学运算时
					
				else:
					num2=int(input("请输入你需要的第二个数值："))
					
					#str(num2).append(user)
					if opration=='+':
						result=num1+num2
					elif opration=='-':
						result=num1-num2
					elif opration=='*':
						result=num1*num2
					elif opration=='/':
						result=num1/num2
					elif opration=='//':
						result=num1//num2
					else:
						result=num1**num2
				a="="
				z=str(num1)+opration+str(num2)+a+str(result)	
				user.append(z)
				users.append(user)
				#打印输出结果
				print("您计算的结果为：%s"%result)
				x=input("按Q键退出计算机,按W键查看历史纪录，按任意键继续：")	
				if x=="Q":
					break
				elif x=="W":
					for u in user:
						print(u)					
					
				else:
					continue
					

			else:
				print("您输入的运算符不合法")
		
	elif option=='2':
		sys.exit(0)
	else:
		input("没有这个选项,按任意键重新选择")
	

