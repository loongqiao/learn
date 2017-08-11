"""
返回上一级菜单

"""
while True:
	print("1.第一章")
	print("1.第二章")
	print("1.第三章")
	print("1.第四章")
	choice=input("请输入你的选项：")
	if choice=='1':
		while True:

			print("第一节，伸展运动")
			user=input("按Z键返回上一级菜单：")
			if user=='Z':
				break
	elif choice=='2':

		while True:

			print("第2节，伸展运动")
			user=input("按Z键返回上一级菜单：")
			if user=='Z':
				break
	elif choice=='3':

		while True:

			print("第3节，伸展运动")
			user=input("按Z键返回上一级菜单：")
			if user=='Z':
				break
	elif choice=='4':
		while True:

			print("第4节，伸展运动")
			user=input("按Z键返回上一级菜单：")
			if user=='Z':
				break
	else:
		print("按任意键继续")


