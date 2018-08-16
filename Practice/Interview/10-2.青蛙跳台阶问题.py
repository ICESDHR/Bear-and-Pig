# -*- coding:utf-8 -*-

# TODO 难点是发现这是一个Fibonacci问题
def JumpFloor(number):
    count = [1,2]
    if number > 2:
        for i in range(2,number):
            count.append(count[i-1]+count[i-2])
    return count[number-1]

# 变态跳台阶问题 青蛙一次可跳无数节台阶
# TODO 不仅可以找出简单的递归规律；还可以变为组合问题，对其进行总结计算
def JumpFloorII(number):
    count = [1, 2]
    for i in range(2, number):
        count.append(2*count[i-1])
    return count[number-1]
# TODO 还可以用位移操作解决，震惊
def JumpFloorII2(number):
    return 2**(number-1)

# 超变态跳台阶问题 青蛙一次最多可跳指定台阶数
def SuperJumpFloor(number,n):
    count = [1,2]
    if number <= n:
        for i in range(2,number):
            temp = sum(count)
            count.append(temp+1)
    else:
        for i in range(2,n):
            temp = sum(count)
            count.append(temp+1)
        for i in range(n,number):
            temp = 0
            for j in range(i-n,i):
                temp += count[j]
            count.append(temp)
    return count[number-1]

if __name__ == '__main__':
    print(JumpFloor(3))
    print(JumpFloorII(3))
    print(JumpFloorII2(3))
    print(SuperJumpFloor(5,3))