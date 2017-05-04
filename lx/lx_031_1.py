#!/usr/bin/env pythton3
# -*- coding:utf-8 -*-

# 打印素数

def _odd():    #存储全体自然数
    n = 1
    while True:
        n = n + 2
        yield n

def guolv(n):  #过滤掉
    return lambda x:x % n > 0

def primes():
    yield 2
    it = _odd()
    while True:
        n = next(it)
        yield n
        it = filter(guolv(n),it)

if __name__ == '__main__':
    x = input('请输入您要打印的素数的最大范围：')
    for i in primes():
        if i < int(x):
            print(i)
        else:
            break
