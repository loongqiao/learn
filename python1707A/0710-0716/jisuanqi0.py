#导入math模块
import math
#用户进行输入
right=True
num1=input("请输入第一个数值： ")
#定义一个参数
result=0

#对输入的数据进行判断
if num1.isdigit():
	num1=int(num1)
	opra=input("请输入运算符号： ")
#对误操作进行剔除
	opra=opra.strip()
	#对运算符进行判定
	if opra=='sin':
		#将弧度转换成度数
		num1=math.radians(num1)
		result=math.sin(num1)

	elif opra=='cos':
		#将弧度转换成度数
		num1=math.radians(num1)
		result=math.cos(num1)

	elif opra=='tan':
		#将弧度转换成度数
		num1=math.radians(num1)
		result=math.tan(num1)
	elif opra=='cot':
		#将弧度转换成度数
		num1=math.radians(num1)
		result=math.cot(num1)
	else:
		num2=input("请输入第二个数值： ")
		if num2.isdigit():
			num2=int(num2)
			if opra=='+':
				result=num1+num2
			else:
				right=False
				print("你特么输入的输入的符号有问题啊 老哥")
		else:
			right=False
			print("你输入的数值有问题啊")

	

else:
	right=False
	print("你特么不会输入数字啊")
if right:	
	print("你的结果是：%s"% result)


