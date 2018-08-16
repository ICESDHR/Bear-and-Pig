# -*- coding:utf-8 -*-

# 求Fibonacci数列的第n项
def Fibonacci1(n):  # 递归方法求Fibonacci
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return Fibonacci1(n-1)+Fibonacci1(n-2)

def Fibonacci2(n):  # 动态规划求Fibonacci，时间复杂度为 O(n)，但是还可以利用矩阵乘法以O(log n)复杂度求得答案
    fibonacci = [0,1]
    if n > 1:
        for i in range(2,n+1):
            fibonacci.append(fibonacci[i-1]+fibonacci[i-2])
    return fibonacci[n]

if __name__ == '__main__':
    print(Fibonacci1(115))
    print(Fibonacci2(115))
