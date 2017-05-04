#!/usr/bin/env python
#检查用户名和PIN码
database = [
    ['admin','admin'],
    ['adminname','1234'],
    ['manage','admin123'],
    ['root','2584']
    ]
username = input ('User Name: ')
pin=input('PIN code: ')

if [username,pin] in database:    #在这里username和pin不能加''。
    print ('Access grated!')
else:
    print ('Please enter current PIN!')
