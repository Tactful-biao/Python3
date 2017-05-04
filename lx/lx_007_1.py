#!/usr/bin/env python
#以正确的宽度在居中的“盒子”内打印一个句子
#输入英文，汉语字节和英语的不一样，如果输入汉语的话，可能会出现对不整齐的现象。
sentence = input ('Please enter some English：')

screen_width=100
text_width=len(sentence)   #len关键字可以求出字符串的长度
box_width=text_width+2
screen_marign=(screen_width - box_width)//2

print
print (screen_marign * ' ' + '+' + box_width * '-' + '+')
print (screen_marign * ' ' + '| ' +(box_width-2) * ' ' + ' |')
print (screen_marign * ' ' + '| ' + sentence + (box_width-text_width-1)*' '+'|')
print (screen_marign * ' ' + '| ' +(box_width-2) * ' ' + ' |')
print (screen_marign * ' ' + '+' + box_width * '-' + '+')
print
