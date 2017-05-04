#!/usr/bin/env python3

# 这段代码会报错，原因是这段代码是用来调试错误的
import pdb
s = '0'
n = int(s)
pdb.set_trace()
print(10 / n)
