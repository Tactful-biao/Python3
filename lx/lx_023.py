#!/usr/bin/env pyrhon3
# -*- coding:utf-8

#把L中的字符大写转小写在L1中输出来

L = ['Hello','Python',18,'Apple',None]
L1 = []
for x in L:
    if isinstance(x,str):
        L1.append(x.lower())
print (L1)
