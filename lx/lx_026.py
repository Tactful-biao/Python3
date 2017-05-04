#!/usr/bin/env python3
#-*- coding:utf-8 -*-

# 打印杨辉三角

def triangles():
    L = [1]
    while True:
        yield L
        L = [L[0]] + [L[i] + L[i+1] for i in range(len(L) - 1)] + [L[-1]]

if __name__ == '__main__':
    n = 0
    x = input ('请输入您要计算的杨辉三角的行数：')
    for t in triangles():
        print(t)
        n = n + 1
        if n == int(x):
            break
