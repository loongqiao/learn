"""


用于管理所有的姑娘
功能：
  查看所有姑娘
  新增一个姑娘
  修改一个姑娘
  删除一个姑娘
  查询不某个姑娘
   退出系统



"""
#打印软件界面

print("#########################################################################")
print("#\t\t世纪佳缘相亲对象管理系统   ")
print("#1.查看所有注册的姑娘")
print("#2.新增一个姑娘")
print("#3.修改指定的姑娘")
print("#4.删除一个指定的姑娘")
print("#5.查看某个指定 的姑娘")
print("#6.退出系统")
print("###########################################################################")

#定义一个保存所有姑娘的列表
girls=[]
while True:
#用户进行选项选择
	choice=input("请输入你的选项： ")
	if choice=='1':
		#利用for循环遍历姑娘
		for name in girls:
			print("姑娘:%s"% name)
	elif choice=='2':
		name=input("请输入你要添加的姓名：")
		girls.append(name)
	elif choice=='3':
		name=input("请输入你需要修改姑娘的姓名：")
		if name in girls:
			index=girls.index(name)
			if index>=0:
				name=input("请输入新的名字： ")
				girls[index]=name
		else:
			print("你输错名字了吧！")

		#判断修改的序号
		"""index=girls.index(name)
		if index >=0:
			name=input("请输入你要修改姑娘的姓名： ")
			girls[index]=name
		else:
			print("抱歉，查无此人")"""
	elif choice=='4':
		name=input("请输入你要删除姑娘的姓名：")
		if name in girls:
			girls.remove(name)
		else:
			print("查无此人")
	elif choice=='5':
		name=input("请输入你需要查看的姑娘：")
		if name in girls:
			print("该姑娘已存在")
		else:
			print("查询不到此人信息")
	elif choice=='6':
		print("客官，慢走")
		break
	else:
		print("没有这个选项")
