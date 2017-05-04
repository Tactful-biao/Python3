#!/usr/bin/env python3
#-*- coding:utf-8

# 写一个计算阶乘的简单的递归函数：有尾递归优化的

def fact(n):
    return fact_iter(n,1)

def fact_iter(number,product):
    if number == 1:
        return product
    return fact_iter(number-1,number * product)

if __name__ == '__main__':
    y = int(input ('请输入您要计算的阶乘：'))
    print (fact(y))
