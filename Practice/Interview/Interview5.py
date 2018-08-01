# -*- coding:utf-8 -*-
# 字符串的空格替换

# 在原字符串上替换
# TODO 注意正序遍历不可以
def ReplaceSpace(s):
    for i in range(len(s)-1,-1,-1):
        if s[i] == ' ':
            s = s[0:i]+'%20'+s[i+1:]
    return s

if __name__ == '__main__':
    S = ['a b c',' a ','a   b','ab','']
    for s in S:
        print(ReplaceSpace(s))