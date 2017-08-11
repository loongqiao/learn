#浏览列表下所有目录文件

#导入os模块
import os
def list_file(path):
    #列出当前目录下所有的子文件
    file_name=os.listdir(path)
    for file in file_name:
        if os.path.isfile(path+os.path.sep+file):
            print("这是一个文件：%s"%file)
        else:
            print("这是一个文件夹：【%s】"%(path+os.path.sep))
            list_file(path)
list_file("e:/py")