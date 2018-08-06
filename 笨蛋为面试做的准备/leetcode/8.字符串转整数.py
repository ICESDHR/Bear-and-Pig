"""
自己的笨办法，基本每种异常情况都用if判断了...
实现 atoi，将字符串转为整数。

在找到第一个非空字符之前，需要移除掉字符串中的空格字符。如果第一个非空字符是正号或负号，选取该符号，并将其与后面尽可能多的连续的数字组合起来，这部分字符即为整数的值。如果第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成整数。

字符串可以在形成整数的字符后面包括多余的字符，这些字符可以被忽略，它们对于函数没有影响。

当字符串中的第一个非空字符序列不是个有效的整数；或字符串为空；或字符串仅包含空白字符时，则不进行转换。

若函数不能执行有效的转换，返回 0。

说明：

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−231,  231 − 1]。如果数值超过可表示的范围，则返回  INT_MAX (231 − 1) 或 INT_MIN (−231) 。

示例 1:

输入: "42"
输出: 42
示例 2:

输入: "   -42"
输出: -42
解释: 第一个非空白字符为 '-', 它是一个负号。
     我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
示例 3:

输入: "4193 with words"
输出: 4193
解释: 转换截止于数字 '3' ，因为它的下一个字符不为数字。
示例 4:

输入: "words and 987"
输出: 0
解释: 第一个非空字符是 'w', 但它不是数字或正、负号。
     因此无法执行有效的转换。
示例 5:

输入: "-91283472332"
输出: -2147483648
解释: 数字 "-91283472332" 超过 32 位有符号整数范围。
     因此返回 INT_MIN (−231) 。
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