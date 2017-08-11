"""
绘制一个菱形
"""
#定义一个变量为行数
rows=1
while rows<=6:
	#定义列数
	sub=1
	while sub <=6-rows:
		print(" ",end='')
		sub +=1
	#定义一个参数为*的数目
	star=1
	while star<=2*rows-1:
		print("*",end="")
		star+=1
	print("")
	rows+=1
rows=1
while rows<=6:
	sub=1
	while sub<=rows:
		print(" ",end="")
		sub+=1
	star=1
	while star<=2*(6-rows)-1:
		print("*",end="")
		star+=1
	print("")
	rows+=1

