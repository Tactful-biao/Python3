#!/usr/bin/env python3
#循环打印1~100，用break提前退出


n = 1
while n <= 100:
    print (n)
    n+=1
    if n > 15:   #当n>15时跳出循环 
        break
print ('The end')
