#!/usr/bin/env python3
#-*- utf-8 -*-

#编写一个prod()函数，可以接受一个list并利用reduce()求积

from functools import reduce

def fn(x,y):
    return x*y
def prod(L):
    return reduce(fn,L)

if __name__ =='__main__':
    print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
