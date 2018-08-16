# -*- coding:utf-8 -*-

# 不使用辅助数据结构判断重复数字
def Dupilcate1(text):
    i = 0
    duplication = set()
    if len(text) <= 0:
        return -1,duplication
    while i < len(text):
        if text[i] < 0 or text[i] > len(text)-1:
            return -1,duplication
        if text[i] != i:
            if text[text[i]] == text[i]:
                duplication.add(text[i])
            else:
                temp = text[text[i]]
                text[text[i]] = text[i]
                text[i] = temp
                i = i-1
        i = i+1
    return 0,duplication

# 不修改原数组
def Dupilcate2(text):
    temp,duplication = set(),set()
    if len(text) <= 0:
        return -1, duplication
    for i in range(len(text)):
        if text[i] < 0 or text[i] > len(text)-1:
            return -1,duplication
        if text[i] in temp:
            duplication.add(text[i])
        else:
            temp.add(text[i])
    return 0,duplication

def HaveDuplicate(text,low,high):
    count = 0
    for item in text:
        if item <= high and item >= low:
            count += 1
    if count > high-low+1:
        return True
    else:
        return False

# 不修改数组也不使用辅助数据结构，不过取值范围为1 ~ n-1
def Dupilcate3(text):
    if len(text) <= 0:
        return -1, set()
    low,high = 1,len(text)-1
    if not HaveDuplicate(text, low, high):
        return -1, set()
    while high > low:
        mid = int((high+low)/2)
        if HaveDuplicate(text,low,mid):
            high = mid
        else:
            low = mid
    return 0,low

if __name__ == '__main__':
    tests = [[1,2,3,4,2,3,1,5],[1,2,3,4,5],[1,2,3,4,6,3,1,5],[]]
    for test in tests:
        flag,duplication1 = Dupilcate1(test.copy())     # python27中list不能使用copy
        flag,duplication2 = Dupilcate2(test.copy())
        flag,duplication3 = Dupilcate3(test.copy())
        if flag:
            print("Wrong Input!")
        else:
            print(duplication1)
            print(duplication2)
            print(duplication3)

