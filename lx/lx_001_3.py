#!/usr/bin/env python
print ('----------标标编程玩游戏------------')

tem = input ('猜猜我心里想的数字：')
guess = int (tem)
if guess > 8:
     print ('哎，老哥，大了大了！\n')
elif guess < 8:
        print ('哎，老哥，小了小了！\n')
while guess != 8:
    tem = input ('猜错了，再来一遍吧：')
    guess = int (tem)
    if guess == 8:
        print ('老哥稳，这都能猜对！')
        print ('猜对也没有奖励 O(∩_∩)O哈哈~')
    elif guess > 8:
            print ('哎，老哥，大了大了！\n')
    else:
        print ('哎，老哥，小了小了！\n')
print ('游戏结束！')
        
