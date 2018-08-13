# 本题为考试多行输入输出规范示例，无需提交，不计分。
#coding=utf-8
import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n, k = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    list1 = list(map(int, line.split()))

    temp = k
    resultlist1 = []
    resultlist2 = []

    while(k>0):
        maxNum = max(list1)
        minNum = min(list1)
        maxIndex = list1.index(max(list1))
        minIndex = list1.index(min(list1))

        if maxNum - minNum == 0:
            break

        if maxNum - minNum == 1:
            break

        list1[maxIndex] -= 1
        list1[minIndex] += 1

        resultlist1.append(maxIndex+1)
        resultlist2.append(minIndex+1)

        k -= 1

    print(max(list1)-min(list1), temp-k)

    for i in range(len(resultlist1)):
        print(resultlist1[i], resultlist2[i])

