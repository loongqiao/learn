row = 1

while row<= 9:
	
	col = 1
	while col <= row:
		print("%s*%s=%s"%(col,row,(row*col)),end="  ")
		col +=1
	row +=1
	print("")