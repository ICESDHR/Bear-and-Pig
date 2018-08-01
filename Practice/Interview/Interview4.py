# -*- coding:utf-8 -*-
# 偏序二维数组中的查找

# 自己做的，很渣改进余地很大
def Find1(target, array):
    if len(array[0]) == 0:
        return False
    elif target < array[0][0] or target > array[len(array)-1][len(array[0])-1]:
        return False
    else:
        for i in range(len(array)):
            if array[i][len(array[i])-1] == target:
                return True
            elif array[i][len(array[i])-1] > target:
                for j in range(len(array[i])):
                    if array[i][j] == target:
                        return True
    return False

def Find2(target, array):
    if len(array[0]) == 0:
        return False
    elif target < array[0][0] or target > array[len(array)-1][len(array[0])-1]:
        return False
    else:
        i = 0
        j = len(array[0])-1
        while i < len(array) and j >= 0:
            if target == array[i][j]:
                return True
            elif target > array[i][j]:
                i = i+1
            else:
                j = j-1
        return False

if __name__ == '__main__':
    target = 11
    array = [[1,3,9,15,20],[2,4,12,19,25],[4,6,15,23,45]]
    print(Find1(target,array))
    print(Find2(target,array))