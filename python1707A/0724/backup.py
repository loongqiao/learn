"""
#文件的备份
"""
#专门用来进行文件备份的函数
import os
def back_file():
    #用户输入
    file_name=input("请输入你要备份的文件名称：")
    #获取文件的名称

    oo=os.path.dirname(file_name)
    pp = os.path.basename(file_name)
    #拆分文件名称，拼接新的文件名称
    new_file_name=oo+"[备份]"+pp

    #读写文件
    old_dile=open(file_name,"br")
    bak_file=open(new_file_name,"bw")

    #开始读写文件
    while True:
        content=old_dile.read(1024*1024)
        if content:
            bak_file.write(content)
        else:
            print("备份完成")
            break

#程序的入口
back_file()