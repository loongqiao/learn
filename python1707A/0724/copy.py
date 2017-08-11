"""
这是一个文件复制的程序
实现文件从一个文件夹复制到另外一个文件夹的
操作
"""
#导入pickle模块
"""import pickle
def read():
    with open ("xx.txt","br")as f:
        xx=pickle.load(f)
def write():
    with open("xx.txt","bw")as f:
        pickle.dump(copy,f)
def copy():
    with open("xx.txt","bc")as f:
        pickle.

write()"""
#创建一个文件复制文件的函数
def copy():
    #要求用户输入源文件路径
    source=input("请输入您要复制的文件名称")
    target=input("请输入你要复制到的地方")
    old_file=open(source,"br")
    new_file=open(target,"bw")
    #开始复制文件 读取文件-》写入新文件
    content=old_file.read()

    new_file.write(content)
    old_file.close()
    new_file.close()

#运行程序
copy()