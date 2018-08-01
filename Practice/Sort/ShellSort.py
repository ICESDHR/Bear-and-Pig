# -*- coding:utf-8 -*-

def ShellSort(a,t):
    while t > 0:
        for i in range(t,len(a)):
            for j in range(i,t-1,-t):
                if a[j] < a[j-t]:
                    a[j],a[j-t] = a[j-t],a[j]
                else:
                    break
        t = t-1
    return a


if __name__ == '__main__':
    t = 3
    a = [1, 7, 3, 9, 14, 2, 5, 9, 6, 10]
    ShellSort(a,t)
    print(a)