#!/usr/bin/env python3

# 这个程序是不能正确运行的，只用来练习抛出异常的
import logging
logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
logging.info('n = %d' % n)
print(10 / n)
