#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 打印回数（正过来和倒过来相同的数 12321、909）

def huishu(n):
    return str(n) == str(n)[::-1]

if __name__ == '__main__':
    x = input('请输入您要打印的回数最大上界：')
    output = filter(huishu,range(1,int(x)))
    print (list(output))
