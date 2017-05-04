#!/usr/bin/env python3
#使用continue语句，跳过当前这个词循环，直接开始下一次循环

n = 0
while n < 10:
    n += 1
    if n == 6:
        continue
    print (n)
print ('The end!')
