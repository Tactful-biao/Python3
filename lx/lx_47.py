#!/usr/bin/env python3

import base64

def safe_base64_decode(s):
    if not len(s) % 4 == 0:
        s = s + b'=' * (4 - len(s) % 4)
    return base64.b64decode(s)

if __name__ == '__main__':
    assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
    assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
    print('Pass')

# assert函数断言是声明其布尔值必须为真的判断，如果发生异常就说明表达式为假。
# 可以理解assert断言语句为raise-if-not，用来测试表示式，其返回值为假，就会触发异常。
