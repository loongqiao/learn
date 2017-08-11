"""
这个是一个百合网的精简版
实现对姑娘的浏览
姑娘信息的修改
姑娘的增删等一系列的操作
可谓是相当完美的一个简易系统
"""
#导入sys模块
import sys

#打印界面 
print("--------------------------------------------------------------------------")
print("\t\t欢迎来到世纪佳缘")
print("\t\t1.浏览系统中存在的所有姑娘")
print("\t\t2.添加一个姑娘")
print("\t\t3.对姑娘的信息进行修改")
print("\t\t4.删除一个姑娘")
print("\t\t5.查看一个特定的姑娘")
print("\t\t6.退出系统")
print("--------------------------------------------------------------------------")

#定义一个空列表，用来存储姑娘的信息
girls=[]
while True:
	#用户选择
	choice=input("请输入你的选项：")
	if choice=='1':
		for name in girls:
			print("姑娘：%s"% name)
			#添加姑娘信息
	elif choice=='2':
		name=input("输入你要添加姑娘的姓名：")
		girls.append(name)
		#查询姑娘信息
	elif choice=='3':
		name=input("请输入你修改姑娘的名字：")
		#判断姑娘是否在list中
		if name in girls:
			#查找姑娘的序列
			index=girls.index(name)
			if index>=0:
				name=input("请输入新的姑娘信息：")
				#将数据存在原来的序列中
				girls[index]=name
		else:
			print("你输错名字了吧")
	#删除选定的姑娘
	elif choice=='4':
		name=input("请输入你要删除的姑娘：")
		#判断姑娘是否在序列中
		if name in girls:
			#删除选定的姑娘
			girls.remove(name)
		else:
			print("查无此人")
	elif choice=='5':
		name=input("请输入你要查看的姑娘：")
		#判断姑娘是否已经存在
		if name in girls:
			print("此姑娘已经存在")
		else:
			print("找不到这个人的信息")
	elif choice=='6':
		print("系统即将退出.....")
		sys.exit(0)
	else:
		print("没有这个选项，请重新输入")

