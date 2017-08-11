"""
这个程序主要实现
文件的备份功能

def backups():
    source=input("请输入你要备份的文件")
    new_file=source+"[备份]"
    original=open(source,"br")6
    new_file=open(new_file,"bw")
    content = original.read()

    new_file.write(content)
    original.close()
    new_file.close()


# 运行程序
backups()"""
def back_file():
    #提示用户
    file_name=input("请输入你要备份的文件名称：")

    dot=file_name.rindex(".")
    sep=file_name.rindex("/")
    name=file_name[sep+1:]
    #拆分文件名称，拼接成新的文件名称
    new_file_name="[备份]"+name

    #读写文件
    old_file=open(file_name,"br")
    bak_file=open(new_file_name,"bw")

    #开始读写文件
    while True:
