#!usr/bin/env python3
#-*- coding:utf-8 -*-

' a test module '  #任何模块的第一个字符串都被视为模块的文档注释

__author__ = 'Michael Biao'  #把作者写进去

import sys     #导入sys模块，利用这个模块，就可以访问sys模块的所以功能

def test():
    args = sys.argv  #sys模块下有一个argv变量，用list存储命令行的所以参数
    if len(args)==1:
        print('Hello, Python!')
    elif len(args) ==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')

if __name__ == '__main__':
    test()
