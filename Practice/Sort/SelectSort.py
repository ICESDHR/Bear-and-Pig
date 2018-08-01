# -*- coding:utf-8 -*-

def SelectSort(a):
    for i in range(len(a)):
        min = a[i]
        index = i
        for j in range(i,len(a)):
            if a[j] < min:
                min = a[j]
                index = j
        a[i],a[index] = a[index],a[i]
    return a


if __name__ == '__main__':
    a = [1, 7, 3, 9, 14, 2, 5, 9, 6, 10]
    SelectSort(a)
    print(a)
