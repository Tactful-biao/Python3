#!/usr/bin/env python3
# 请定义一个函数quadratic(a,b,c)，接收3个参数，返回一元二次方程：
# ax2 + bx + c = 0的两个解

import math

def quadratic(a,b,c):
    
    if (b * b - 4 * a * c) < 0:
        print ('无解')
    elif (b * b - 4 * a * c) == 0:
        print ((-b+math.sqrt(b * b - 4 * a * c))/(2*a))
    else:
        print ((-b+math.sqrt(b * b - 4 * a * c))/(2*a))
        print ((-b-math.sqrt(b * b - 4 * a * c))/(2*a))

if __name__ == '__main__':
    x = int(input('请输入系数a:'))
    y = int(input('y请输入系数b:'))
    z = int(input('y请输入常数c:'))
    print (quadratic(x,y,z))
