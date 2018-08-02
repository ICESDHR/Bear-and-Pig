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