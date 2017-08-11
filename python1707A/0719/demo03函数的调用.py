"""
声明定义函数
"""
def closewindow():
	print("关闭窗户")

def buyqi(money):
	print("卖了%s元的气球"%money)

def qukuaidi():
	print("帮我取快递")
	return "给你"
def huodao(money):
	print("帮我取%s的快递"%money)
	return "结束"
closewindow()
print("=============================")
buyqi(100)
print("=============================")
box=qukuaidi()
print("%s"%box)
print("=============================")
boxs=huodao(100)
print("%s"%boxs)
