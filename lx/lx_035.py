#!/usr/bin/env python3
# -*- coding:utf-8 -*-

# 利用@property给一个Screen对象加上width和height属性，以及一个只读属性resolution

class Screen(object):
    @property
    def width(self):
        return self._width
    @width.setter
    def width(self,value):
        if not isinstance(value,int):
            raise ValueError('Width must be integer!')
        if value < 0:
            raise ValueError('Width must be > 0')
        self._width = value

    @property
    def height(self):
        return self._height
    @height.setter
    def height(self,value):
        if not isinstance(value,int):
            raise ValueError('Height must be integer!')
        if value < 0:
            raise ValueError('Height must be > 0')
        self._height = value

    @property
    def resoultion(self):
        return self._width * self._height
    
