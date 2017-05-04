#!/usr/bin/env python
a=[
    ['admin','password']
    ]
b=input('admin: ')
p=input('password: ')
if [b,p] in a:
    print('Access grated!')
else:
    print('Sorry!')
