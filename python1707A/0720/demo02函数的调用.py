def baidu(keyword):
	print("搜索关键词：%s"%keyword)
	z=input("搜索完成，点击查看")
	if z=="1":
		buy()
	if z=="2":
		find()
	else:
		print("重新搜索")
		baidu()
def buy():
	c=input("够买火车票")
	if c=="R":
		baidu("购买跳转回来")
def find():
	c=input("查询火车票")
	if c=="R":
		baidu("查询跳转回来")

baidu("火车票")
