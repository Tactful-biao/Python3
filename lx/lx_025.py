#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 打印斐波那契数列的函数

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        print (b)
        a,b = b,a + b
        n = n + 1
    return ('Done')

if __name__ == '__main__':
    x = input('请输入你要显示的斐波那契数列长度：')
    print(fib(int(x)))
    
