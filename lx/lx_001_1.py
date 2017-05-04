#!/usr/bin/env python
#猜数字游戏改进
print('-------------------标标带你玩游戏-----------------')
tem = input("请猜一下我心里在想哪一个数字：")
guess = int(tem)
if guess == 8:
    print ('哇塞，这都能猜对，你好棒棒哦！')
    print ('猜对也没有奖励！O(∩_∩)O哈哈~')
else:
    if guess > 8:
        print ('猜错了哦，比正确答案大！')
    else:
        if guess < 8:
            print('猜错了哦，比正确答案小！')
print ('游戏结束。')
