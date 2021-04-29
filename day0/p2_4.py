#p2_1.py
"""---第一个小程序---"""
import random

secret=random.randint(0,9)
temp=input("不妨猜一下小甲鱼现在心里相的是哪个数字：")
guess=int(temp)
while guess!=secret:
    print("猜错啦，再来！")
    temp=input()
    guess=int(temp)
    
if secret==guess:
    print("你是小甲鱼肚子里的蛔虫吗?!")
    print("哼，猜中了也没奖励！")
else:
    if guess>secret:
        print("哥，大了大了~~~")
    else:
        print("嘿，小了小了~~~")

print("游戏结束，不于啦^-^")
