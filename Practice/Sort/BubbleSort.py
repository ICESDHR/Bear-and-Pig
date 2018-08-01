# -*- coding:utf-8 -*-

def BubbleSort(a):
    for i in range(len(a)-1):
            flag = 1
            for j in range(len(a)-1-i):
                if a[j] > a[j+1]:
                    a[j],a[j+1] = a[j+1],a[j]
                    flag = 0
            if flag:
                break
    return a


if __name__ == '__main__':
    a = [1, 7, 3, 9, 14, 2, 5, 9, 6, 10]
    BubbleSort(a)
    print(a)