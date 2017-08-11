#打印界面

print("/////////////////////////////////////")
print("\t\t计算器")
print("/////////////////////////////////////")
num=input("请输入数值：")
try:
    num_int=int(num)
except ValueError as e:
    print("对不起，您输入录入非法字符%s"%e)
else:
    print("用户输入的数据为%s"%num_int)