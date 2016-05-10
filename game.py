#coding:utf-8
import random
print ('------------我爱番茄帝工作室---------------')
temp = input ("不妨猜一下番茄帝现在心里想的是哪个数字:")
guess = int(temp)
while (guess !=8,a<3):
    temp = input("答错了，再来一次吧，请输入:")
    guess = int(temp)
    if guess == 8:
        print("我CAO,你是番茄帝心里的蛔虫吗?!")
        print("哼,猜中了也没有奖励!")

    else :
        a=a+1
        if guess < 8:
            print ("嘿嘿，小了，小了。")
        else:
            if guess >8:
                print("大了，大了。")
        #print("猜错啦,番茄帝现在心里想的是8!")
print("游戏结束，不跟你玩了^_^!")
