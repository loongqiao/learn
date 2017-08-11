msg="Hello,my world"
#将程序中的数据写入到计算机的文件中

#打开文件
f=open("e:/python1707A/0721/text.txt","w") #write
#写入数据
f.write(msg)
#关闭文件
f.close()
#读取计算机中的文件中 的数据，到程序中展示
f=open("e:/python1707A/0721/text.txt","r") #read
#读取数据
m=f.read()
#展示数据
print("%s"%m)
#关闭文件
f.close()
