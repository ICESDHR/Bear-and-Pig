# -*- coding:utf-8 -*-

def QuickSort1(a):
    if len(a) <= 1:
        return a
    flag,index = -1,0
    pivotkey = a[-1]
    for i in range(len(a)-1):
        if a[i] > pivotkey:
            flag = i
        else:
            index = i+1
            if flag >= 0:
                index = flag+1
                a[i],a[flag] = a[flag],a[i]
                flag = i
    a[index], a[len(a)-1] = a[len(a)-1], a[index]
    return QuickSort1(a[0:index]) + QuickSort1(a[index:len(a)])


def QuickSort2(a):
    if len(a) <= 1:
        return a
    if a[1] > a[0]:
        pivotkey = a[1]
        a[1], a[len(a)-1] = a[len(a)-1],a[1]
    else:
        pivotkey = a[0]
        a[0], a[len(a)-1] = a[len(a)-1],a[0],
    i = 0; j = len(a)-2
    flag1,flag2 = 0,0
    while i <= j:
        if flag1 and flag2:
            a[i],a[j] = a[j],a[i]
            flag1,flag2 = 0,0
        if a[i] <= pivotkey:
            i = i+1
        else:
            flag1 = 1
        if a[j] > pivotkey:
            j = j-1
        else:
            flag2 = 1
    a[i],a[len(a)-1] = a[len(a)-1],a[i]
    return QuickSort2(a[0:i]) + QuickSort2(a[i:len(a)])


if __name__ == '__main__':
    a = [1, 7, 3, 9, 14, 2, 5, 9, 6, 10]
    b = QuickSort1(a.copy())
    c = QuickSort1(a.copy())
    print(b)
    print(c)
