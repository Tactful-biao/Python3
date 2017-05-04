#!/usr/bin/env python3
# 小明身高1.75，体重80.5kg。请根据BMI公式（体重(kg)除以身高(m)的平方）帮小明计算他的BMI指数，并根据BMI指数：
# 低于18.5：过轻
# 18.5-25：正常
# 25-28：过重
# 28-32：肥胖
# 高于32：严重肥胖

# 改进版：提供自助查询，输入自己的身高和体重，然后会告诉你查询结果
x = input ('请输入你的体重(kg)：')
weight = float (x)  #注意这里的体重需要用转换成浮点数
y = input ('请输入你的身高(m)：')
height = float(y)    #注意这里的身高也需要用转换成浮点数

BIM = weight / (height * height)

if BIM < 18.5:
    print ('过轻！')
elif BIM < 25:
    print ('正常！')
elif BIM < 28:
    print ('过重！')
elif BIM < 32:
    print ('肥胖！')
else:
    print ('严重肥胖！')
