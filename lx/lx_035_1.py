#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 对于斐波那契数列，通过切片的方式访问

class Fib(object):
    def __getitem__(self,n):
        if isinstance(n,int):
            a ,b = 1,2
            for i in range(n):
                a , b = b , a + b
            return a
        if isinstance(n,slice):
            start = n.start
            stop = n.stop
            if start is None:
                start = 0
            a,b = 1,1
            L = []
            for i in range(stop):
                if i >= start:
                    L.append(a)
                a , b = b , a + b
            return L
