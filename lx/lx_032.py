#!/usr/bin/env pythton3
# -*- coding:utf-8 -*-

#过滤掉非回数（从左向右读和从右往左读一样的数，例如12321,909）
#使用filter()过滤掉非回数

 
def is_palindrome(n):
    return str(n) == str(n)[::-1]  #利用切片，回数是正过来和倒过来相等

if __name__ == '__main__':
    x = input ('请输入你要计算回数的最大范围：')
    output = filter(is_palindrome,range(1,int(x)))
    print (list(output))
