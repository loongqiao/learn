"""
查找特定的文件或者文件夹

"""
files=[]
#导入模块
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
def search(keywords,path):

    list_file(path)
    for fl in file_list:

        if fl.find(keywords)>=0:
            kw_list.append(fl)
    return kw_list
k_l=search("r","e:/python1707A")
