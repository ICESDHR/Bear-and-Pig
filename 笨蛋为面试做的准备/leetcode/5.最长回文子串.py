'''
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为1000。

示例 1：

输入: "babad"
输出: "bab"
注意: "aba"也是一个有效答案。
示例 2：

输入: "cbbd"
输出: "bb"
'''

"""
暴力解法。。。
"""
def Palindrome1(s):
    slen = len(s)
    i = 0
    j = slen-1
    while(i < j):
        if(s[i] != s[j]):
            return 0
        i += 1
        j -= 1
    return len(s)

def longestPalindrome1(s):
    slen = len(s)
    maxstr = ""
    maxlen = 0
    for i in range(0, slen):
        for j in range(i, slen):
            curlen = Palindrome1(s[i:j+1])
            if curlen >= maxlen:
                maxlen = curlen
                maxstr = s[i:j+1]
    return maxstr

"""
以轴对称的解法
"""

'''
Manacher 算法
https://segmentfault.com/a/1190000003914228
'''
def longestPalindrome2(s):
    #预处理
    s='#'+'#'.join(s)+'#'

    RL=[0]*len(s)
    MaxRight=0
    pos=0
    MaxLen=0

    curindex = 0
    for i in range(len(s)):
        if i<MaxRight:
            RL[i]=min(RL[2*pos-i], MaxRight-i)
        else:
            RL[i]=1
        #尝试扩展，注意处理边界
        while i-RL[i]>=0 and i+RL[i]<len(s) and s[i-RL[i]]==s[i+RL[i]]:
            RL[i]+=1
        #更新MaxRight,pos
        if RL[i]+i-1>MaxRight:
            MaxRight=RL[i]+i-1
            pos=i
        #更新最长回文串的长度
        if RL[i] >= MaxLen:
            MaxLen = RL[i]
            curindex = i
    # return MaxLen-1
    return s[curindex-MaxLen+1:curindex+MaxLen-1].replace('#', '')

"""
动态规矩方法
"""
def longestPalindrome(s):
    n = len(s)
    # pal[i][j] 表示s[i...j]是否是回文串
    pal = [[0 for _ in range(n+1)]for _ in range(n+1)] #二维数组的初始化 要记住！！！
    maxLen = 0
    maxstr = ""
    for i in range(0, n): # i作为终点
        j = i # j作为起点
        while(j>=0):
            if(s[j]==s[i] and (i-j<2 or pal[j+1][i-1])):
                pal[j][i]=1
                # maxLen=max(maxLen, i-j+1);
                if(i-j+1 > maxLen):
                    maxLen = i-j+1
                    maxstr = s[j:i+1]
            j -= 1
    return maxstr

if __name__=="__main__":
    print(longestPalindrome("a"))