'''
因数
时间限制：C/C++语言 1000MS；其他语言 3000MS
内存限制：C/C++语言 65536KB；其他语言 589824KB
题目描述：
给出一个正整数n，求10^18以内含有n个因数的最小的正整数是多少？

输入
输入仅包含一个正整数n，表示因数的数量(1<=n<=1000)。

输出
对于每组数据输出一行，仅有一个数字，即小于等于10^18中含有n个因数的最小的正整数。


样例输入
4
样例输出
6
'''
def allFactor(num_intput):
    if num_intput == 1:
        return 1
    num_factors = 2
    search = num_intput // 2
    i = 2
    while i <= search:
        if num_intput % i == 0:
            if num_intput // i > i:
                num_factors += 2
            elif num_intput // i == i:
                num_factors += 1
            else:
                break
        i += 1
    return num_factors

if __name__ == '__main__':
    n = int(input())
    lst = [0]
    for i in range(1, 10**18):
        tmp = allFactor(i)
        lst.append(tmp)
        if n == tmp:
            print(i)
            break
