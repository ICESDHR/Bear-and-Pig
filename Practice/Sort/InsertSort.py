# -*- coding:utf-8 -*-

def InsertSort(a):
    for i in range(1,len(a)):
        for j in range(i,0,-1):
            if a[j] < a[j-1]:
                a[j],a[j-1] = a[j-1],a[j]
            else:
                break
    return a


if __name__ == '__main__':
    a = [1, 7, 3, 9, 14, 2, 5, 9, 6, 10]
    InsertSort(a)
    print(a)
