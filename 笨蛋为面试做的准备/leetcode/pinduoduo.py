#coding=utf-8
import sys
if __name__ == "__main__":
    # 读取第一行的n
    st = sys.stdin.readline().strip()
    stlen = len(st)
    if stlen==0:
        print(0)

    for i in range(0, stlen):
        j = 0
        result = st[:i+1]
        while(j<stlen and st[j]==result[j%len(result)]):
            i+=1
            j+=1
        if(j==stlen):
            print(result)
            break