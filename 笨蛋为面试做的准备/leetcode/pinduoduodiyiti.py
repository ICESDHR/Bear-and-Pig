#coding=utf-8
import sys
if __name__ == "__main__":
    s = sys.stdin.readline().strip().strip("[]").replace(',', '')
    n = len(s)
    if n<3:
        print(0)
        exit()
    maxLen = 0
    maxstr = ""
    for i in range(1, n):
        j=i-1
        k=i+1
        temp = i
        while(j>=0):
            if(s[j]>s[temp]):
                temp = j
                j -= 1
            else:
                j += 1
                break
        if(j<0):
            j = 0
        temp = i
        while(k<n):
            if(s[k]>s[temp]):
                temp = k
                k += 1
            else:
                k -= 1
                break
        if(k>=n):
            k=n-1
        if(k-j+1 > maxLen):
            maxLen = k-j+1
            maxstr = s[j:k+1]
    if(maxLen>=3):
        print(maxLen)
    else:
        print(0)
