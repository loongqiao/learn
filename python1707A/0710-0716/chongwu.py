"""
热销商品
"""
#导入界面
import os 
import sys
os.system("cls")
set1=set({})
while True:
	
	
	
	#打印界面
	print("--------------------------------------------------")
	print("\t1.查看所有热销产品")
	print("\t2.查看所有商品")
	print("\t3.查询该商品是否下架")
	print("\t4.删除商品")
	print("\t5.修改商品")
	print("\t6.上架新商品")
	print("\t7.退出页面")
	print("--------------------------------------------------")
	choice=input("请输入您的选项：")
	if choice=="1":
		for i in set1:
			print("热销商品：%s"% i)
	elif choice=='2':
		for i in set1:
			print("所有商品为：%s"% i)
	elif choice=="3":
		sp=input("请输入你要查询的商品：")
		if sp in set1:
			print("该商品还在销售")
		else:
			print("该商品已经下架")
	elif choice=="4":
		sp=input("请输入你要删除的商品：")
		if sp in set1:
			set1.discard(sp)
			input("删除成功按任意键继续")

	elif choice=="5":
		sp=input("请输入你要更改的商品名字")
		if sp in set1:
			ssp=input("请输入新商品的名字：")
			set1.discard(sp)
			set1.add(ssp)
			input("修改成功，按任意键继续")
		else:
			input("您输入的商品不存在，按任意键继续：")
	elif choice=="6":
		sp=input("请输入你要上架的商品：")
		set1.add(sp)
		input("商品上架成功，按任意键继续")
	elif choice=="7":
		print("系统即将退出.....")
		sys.exit(0)
	else:
		input("没有这个选项，按任意键继续")