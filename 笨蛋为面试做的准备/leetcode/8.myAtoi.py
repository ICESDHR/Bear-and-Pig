"""
自己的笨办法，基本每种异常情况都用if判断了...
"""
def myAtoi1(str):
    while len(str)>=1 and str[0] == " ":
        str = str[1:]
    if len(str)==0:
        return 0
    if str[0]=="+":
        str=str[1:]
        if "-" in str:
            return 0
    if len(str)==0:
        return 0
    if str[0] not in "-0123456789":
        return 0
    elif str[0] == "-":
        if len(str)==1:
            return 0
        else:
            i = 1
            while i<=len(str)-1 and str[i] in "0123456789":
                i+=1
            try:
                result = int(str[:i]) ###
            except:
                return 0
    else:
        i = 0
        while i<=len(str)-1 and str[i] in "0123456789":
            i += 1
        result = int(str[:i])  ###

    if result > 2**31-1:
        return 2**31-1
    elif result < -2**31:
        return -2**31
    else:
        return result
"""
大神的方法
注意了！strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列!!!头尾！
"""
def myAtoi(str):
    if len(str) == 0: return 0
    ls = list(str.strip())
    print(ls)
    # sign = -1 if ls[0] == '-' else 1
    if ls[0] == '-':
        sign = -1
    else:
        sign = 1
    if ls[0] in ['-', '+']: del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ret = ret * 10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))

if __name__=="__main__":
    print(myAtoi("   -42 "))