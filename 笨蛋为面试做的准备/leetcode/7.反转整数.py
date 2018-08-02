'''
给定一个 32 位有符号整数，将整数中的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
注意:

假设我们的环境只能存储 32 位有符号整数，其数值范围是 [−2**31,  2**31 − 1]。根据这个假设，如果反转后的整数溢出，则返回 0。
'''
def reverse(x):
    xstr = str(x)
    if xstr[0] == "-":
        result = int(xstr[0]+xstr[1:][::-1])
    else:
        result = int(xstr[::-1])
    if result < -1 * pow(2, 31) or result > pow(2, 31) - 1:
        return 0
    else:
        return result


if __name__=="__main__":
    print(reverse(1534236469))