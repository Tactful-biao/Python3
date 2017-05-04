#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#利用map()函数，把用户输入的不规范的英文名字，变成首字母大写，其他小写的规范名字
# 输入：['admin','LISA','barT'],输出:['Admin','List','Bart']

def normalize(name):
    return name.title()

if __name__ == '__main__':
    L1=['admin','LISA','barT']
    L2 = list(map(normalize,L1))
    print(L2)
