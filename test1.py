
#第一题
count = 0
count1=0
count2=0
for i in range(101):
    count=count+i
    print("1-100之和为：",count)
    if i%2==0:
        count1 = count1+i
        print("1-100偶数之和为：",count1)

    else:
        count2 = count2+i
        print("1-100奇数之和为：",count2)



#3)直接用for循环，实现1~100的偶数之和
count3 = 0
for j in range(0,101,2):
    count3 = count3+j
    print("直接用for循环输入1-100偶数之和",count3)


#第二题-猜数字游戏

import random
a =random.randint(1,100)
while True:
    b = int(input("请输入数字"))
    if b>a:
        print("小一点")
        continue
    elif b<a:
        print("大一点")
        continue
    else:
        print("猜对了")
        break






