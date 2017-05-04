#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 以斐波那契数列为例，写一个Fib类，可用作for循环

class Fib(object):
    def __init__(self):
        self.a,self.b = 0,1  #初始化两个计数器a，b

    def __iter__(self):
        return self    #实例本身就是迭代器，故返回自己

    def __next__(self):
        self.a,self.b = self.b, self.a + self.b   #返回下一个值
        if self.a > 100000: #退出循环的条件
            raise StopIteration()
        return self.a  #返回下一个值
