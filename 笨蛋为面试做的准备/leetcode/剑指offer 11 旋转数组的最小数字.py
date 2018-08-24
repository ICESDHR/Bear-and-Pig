def minNumberInRotateArray(rotateArray):
    if len(rotateArray) < 1:
        return
    if len(rotateArray) == 1:
        return rotateArray[0]
    start = 0
    end = len(rotateArray) - 1
    mid = (start + end) // 2
    if rotateArray[start] <= rotateArray[mid] and rotateArray[mid] >= rotateArray[end]:
        return minNumberInRotateArray(rotateArray[mid+1:])
    else:
        return minNumberInRotateArray(rotateArray[:mid+1])

if __name__ == "__main__":
    print(minNumberInRotateArray([3,4,5,1,2]))