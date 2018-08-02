#coding=utf-8
import sys
import operator;
if __name__ == "__main__":
    a = input().split()
    N = int(a[0])
    K = int(a[1])
    n = sys.stdin.readline().strip()
    nlen = len(n)
    lst = []
    for i in range(0, nlen):
        lst.append(int(n[i]))
    # print(a, lst)
    # print(lst)
    num=0
    mincost = 1000
    minstr = ""
    for i in range(0, 10):
        temp = 0
        for j in lst:
            temp += abs(j-i)
        if temp < mincost:
            num = i
            mincost = temp

    lst1 = []
    for i in range(0, nlen):
        lst1.append([abs(num-lst[i]), i])
    lst1.sort()
    for i in range(K):
        if lst1[i][1]>0:
            lst[i] = num
    result = ""
    for i in range(nlen):
        result+=str(lst[i])
    print(mincost)
    print(result)
