#!/usr/bin/env python3
# 利用os模块编写一个能实现dir -l输出的程序
# 就是让打印文件夹里面文件的属性。包括权限，文件数，用户名...
import os
import time

def listFile(path):
    print('权限\t\t文件数\t\t用户名\t\t群组名\t\t大小\t\t  月份\t\t日期\t\t时间\t\t\t文件名')
    for x in os.listdir(path):
        dir = os.path.join(path,x)
        st = os.stat(dir)
        print(oct(st.st_mode)[-3:],end='\t\t  ')
        print(numOfFiles(dir),end='\t\t\t  ')
        print(st.st_uid,end='\t\t\t  ')
        print(st.st_gid,end='\t\t\t')
        print(st.st_size,end='\t\t  ')
        lc_time = time.localtime(st.st_mtime)
        print(time.strftime('%b',lc_time),end='\t\t')
        print(lc_time.tm_mday,end='\t\t')
        print(time.strftime('%H:%M',lc_time),end='\t\t')
        print(x)

#计算文件夹数，最小为1
def numOfFiles(path,num=1):
    try:
        for x in os.listdir(path):
            dir = os.path.join(path,x)
            if os.path.isdir(dir):
                num+=1
                num=numOfFiles(dir,num)
    except BaseException as e:
        pass
    finally:
        return num
if __name__ == '__main__':
    dirpath = r'D:\Python练习\lx'
    listFile(dirpath)