import os
#文件读取
def s_read(file):
    with open(file,'r') as f1:
        listline=f1.readlines()
    return listline
#文件写入
def s_write(file,listline):
    with open(file,'w') as f1:
        for i in listline:
            f1.write(i+'\n')

