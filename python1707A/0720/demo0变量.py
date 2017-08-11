"""
全局变量和局部变量
"""
he=0
if True:
	print("if中访问全局变量：%s"% he)
while True:
	print("循环中访问的全局变量：%s"%he)
	break
def func():
	she=12
	print("函数中华访问全局变量:%s"%she)
	print("函数中访问自己的局部变量是%s"%she)
def other():
	print("other函数中访问func函数的局部变量是：%s"%she)
func()
print("直接在程序中，访问func()函数的局部变量：%s"% she)
other()