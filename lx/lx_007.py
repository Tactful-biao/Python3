#!/usr/bin/env python
#以正确的宽度在居中的“盒子”内打印一个句子
#注意，整数除法运算符（//）只能用在Python2.2以及后续版本，在之前的版本中，只能用普通的处罚（/)
sentence = input ("Sentence: ")

screen_width=80   #定义屏幕的宽度
text_width=len(sentence)   #输入的文本长度
box_width=text_width+6    #盒子的长度
left_margin=(screen_width-box_width)//2   #定义离左边窗口的距离 
print
print (' ' * left_margin + '+' + '-'*(box_width-3)+'+')
print (' ' * left_margin + '| ' + ' '*(text_width-1) + '   |')
print (' ' * left_margin + '| ' +    sentence     +'  |')
print (' ' * left_margin + '| ' + ' ' *(text_width-1) +'   |')
print (' ' * left_margin + '+' +'-' *(box_width-3)+ '+')
print
