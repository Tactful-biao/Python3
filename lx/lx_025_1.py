#/usr/bin/env python3
# -*- coding:utf-8 -*-

def fib(max):
    n,a,b = 0,0,1
    while n < max:
        yield b       #生成器遇到yield中断
        a,b = b, a + b
        n = n + 1

if __name__ == '__main__':
    x = input ('请输入你要列出的斐波那契若数列个数：')
    for n in fib(int(x)):
        print (n)
