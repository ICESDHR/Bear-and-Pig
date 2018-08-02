'''
给定一个字符串，找出不含有重复字符的最长子串的长度。

示例：

给定 "abcabcbb" ，没有重复字符的最长子串是 "abc" ，那么长度就是3。

给定 "bbbbb" ，最长的子串就是 "b" ，长度是1。

给定 "pwwkew" ，最长子串是 "wke" ，长度是3。请注意答案必须是一个子串，"pwke" 是 子序列  而不是子串。
'''
def lengthOfLongestSubstring(s):
    slen = len(s)
    maxlen = 0
    curlen = 0
    position = [-1 for _ in range(256)]
    for i, char in enumerate(s):
        if position[ord(char)] >= 0:
            d = i - position[ord(char)]
            position[ord(char)] = i
            if d > curlen:
                curlen += 1
            if d <= curlen:
                curlen = d
        else:
            curlen += 1
            position[ord(char)] = i
        if curlen > maxlen:
            maxlen = curlen
    return maxlen

if __name__=="__main__":
    print(lengthOfLongestSubstring("abcabcbb"))