"""
绘制一个金字塔

----*----
---***---
--*****--
-*******-
*********
"""

row=1

while row<=5:
	
	col=1
	while col<=(5-row):
		print(" ",end='')
		col +=1
		
	star=1	
	while star<=2*row-1:

		print("*",end='')
		star+=1
	print(" ")
	row +=1
