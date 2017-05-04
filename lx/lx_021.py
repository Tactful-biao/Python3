#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#汉诺塔的移动可以用递归函数非常简单的实现
#请编写move(n, a, b, c)函数，它接收参数n，
#表示3个柱子A、B、C中第1个柱子A的盘子数量，然后打印出把所有盘子从A借助B移动到C的方法。

def move(n,a,b,c):
    if n == 1:
        print ('move',a,'-->',c)
        return
    move(n-1,a,c,b)
    print('move',a,'-->',c)
    move(n-1,b,a,c)

if __name__ == '__main__':
    x=int(input('请输入汉诺塔盘子的数量：'))
    move (x,'A','B','C')
