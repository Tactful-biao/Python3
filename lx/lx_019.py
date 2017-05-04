#!/usr/bin/env python3
# -*- coding:utf-8 -*-

#给定一组数字a，b，c，...，计算它们的平方和

def cacl(*numbers):   #number前面加上*表示可变参数，不加的话表示不可变
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
