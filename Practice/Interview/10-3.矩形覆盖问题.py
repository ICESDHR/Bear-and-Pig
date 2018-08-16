# -*- coding:utf-8 -*-

# TODO 反应不过来是Fibonacci问题
def RectCover(number):
    count = [0,1,2]
    if number > 2:
        for i in range(3,number+1):
            count.append(count[i-1]+count[i-2])
    return count[number]