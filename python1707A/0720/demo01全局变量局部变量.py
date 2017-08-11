"""
全局变量和局部变量
"""
#定义一个全局变量

it=10
def qq():
	global it
	print("全局变量是：%s"%it)
	it+=10
	print("全局变量是：%s"%it)
qq()
print("全局变量是：%s"%it)
import math
#计算园周长
def yuan(r):
	c=2*math.pi*r
	return c
c1=yuan(10)
c2=yuan(20)
print("%s,%s"%(c1,c2))