# -*- coding:utf-8 -*-

# 旋转数组的最小数字
def MinNumberInRotateArray(rotateArray):
    if len(rotateArray) == 0:
        return 0
    elif len(rotateArray) == 1:
        return rotateArray[0]
    elif len(rotateArray) == 2:
        if rotateArray[0] < rotateArray[1]:
            return rotateArray[0]
        else:
            return rotateArray[1]
    else:
        length = len(rotateArray)
        if rotateArray[0] >= rotateArray[length-1]:
            mid = int(length/2)
            if rotateArray[mid] < rotateArray[0]:
                return MinNumberInRotateArray(rotateArray[1:mid+1])
            elif rotateArray[mid] > rotateArray[0]:
                return MinNumberInRotateArray(rotateArray[mid+1:])
            else:
                return min(MinNumberInRotateArray(rotateArray[:mid]),MinNumberInRotateArray(rotateArray[mid+1:]))
        else:
            return rotateArray[0]

if __name__ == '__main__':
    rotateArray = [3,3,3,3,3,0,3]
    print(MinNumberInRotateArray(rotateArray))