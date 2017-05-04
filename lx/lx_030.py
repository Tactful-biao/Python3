#!/usr/bin/env python3
#-*- utf-8 -*-

# 利用map()和reduce()编写一个str2float函数，把字符串转换成浮点数123.456：
from functools import reduce

def fn(x,y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]  
def str2float(s):
    return reduce(fn, map(char2num,s.replace('.','')))

if __name__ == '__main__':
    s = input('请输入一个浮点数:')
    #s='123.456'
    if s.find('.')!=-1:
        print('str2float(\'%s\')=' %s, str2float(s)/pow(10,(len(s)-s.find('.')-1)))
    else:
        print ('str2float(\'%s\') ='%s, str2float(s))
    
