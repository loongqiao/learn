"""
这是一个简单的火车站售票
"""
ticketCount=100
while ticketCount>0:
	ticketCount -=1
	print("卖出%s张票，剩余%s张票" % ((100-ticketCount),ticketCount))

	if ticketCount<=30:
		print("发生暴动，下班")
		break
else:
	print("下班回家")

