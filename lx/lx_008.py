#!/usr/bin/env python
#检查用户名和PIN码
database = [
    ['albert','1234'],
    ['dilbert','4242'],
    ['dilbert,'7514'],
    ['jones','9843']
    ]
username = input('User name: ')
pin=input('PIN: code: ')

if [username,pin] in database:
    print ('Access grated!')
else:
    print ('Please enter currect PIN!')
