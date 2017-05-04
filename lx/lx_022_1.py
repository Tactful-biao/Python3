#!/usr/bin/env python3
#-*- coding:utf-8

#构造一个1,3,5,7...99的列表  for循环的方法

L=[]

for i in range(1,100):
    if (i % 2 == 1):
        L.append(i)
print (L)
