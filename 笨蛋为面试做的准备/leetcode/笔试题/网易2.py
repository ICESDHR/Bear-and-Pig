# 本题为考试多行输入输出规范示例，无需提交，不计分。
#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    line = sys.stdin.readline().strip()
    n, k = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    list1 = list(map(int, line.split()))

    line = sys.stdin.readline().strip()
    # 把每一行的数字分隔后转化成int列表
    list2 = list(map(int, line.split()))

    count = 0
    for i in range(n):
        if list2[i] == 1:
            count += list1[i]
    maxcount = count
    for j in range(n-k+1):
        temp = count
        for l in range(k):
            if list2[j+l] == 0:
                temp += list1[j+l]
        if temp > maxcount:
            maxcount = temp

    print(maxcount)