"""
由于计算机内存有限所以对大文件
进行分开处理

"""
def copy():
    #提示用户输入原文件名称
    source=input("请输入源文件名称")
    target=input("请输入目标文件名称")

    #打开文件
    old_file=open(source,"br")
    new_file=open(target,"bw")

    #复制文件
    while True:
        contennt=old_file.read(1024*1024)
        if contennt:
            new_file.write(contennt)
        else:
            print("文件复制完成")
            break

    #关闭文件
    old_file.close()
    new_file.close()
#程序的入口
copy()