#正确答案https://blog.csdn.net/marlonlyh/article/details/70799152?utm_source=itdadao&utm_medium=referral
#这题没写完...11 和 10 这两种情况没考虑
def createPalindrome(n, odd):
    nlen = len(n)
    if odd == 0:#偶数
        lst = [0 for _ in range(2*nlen)]
        for i in range(0, nlen):
            lst[i] = n[i]
            lst[2*nlen-1-i] = n[i]
        return lst
    if odd == 1:#奇数
        lst = [0 for _ in range(2*(nlen-1)+1)]
        lst[nlen-1] = n[nlen-1]
        for i in range(0, nlen-1):
            lst[i] = n[i]
            lst[2*(nlen-1)-i] = n[i]
        return lst

def listToint(n):
    nlen = len(n)
    num=0
    for i in range(nlen):
        num += int(n[nlen-1-i])*pow(10,i)
    return num

def nearestPalindromic(n):
    nstr = n
    lst = list(n)
    nLen = len(n)
    if nLen == 1:
        return str(int(n)-1)
    if nLen % 2 == 0:
        temp = listToint(lst[:nLen//2])
        result1 = listToint(createPalindrome(n[:nLen//2], 0))
        result2 = listToint(createPalindrome(str(temp+1), 0))
        # print(result1, result2)
    else:
        temp = int(n[:nLen//2+1])
        result1 = listToint(createPalindrome(n[:nLen // 2+1], 1))
        result2 = listToint(createPalindrome(str(temp + 1), 1))
    print(result1, result2)
    if abs(result1 - int(n)) == abs(result2 - int(n)):
        if result1 < result2:
            return str(result1)
        else:
            return str(result2)
    if abs(result1 - int(n)) < abs(result2 - int(n)):
        return str(result1)
    else:
        return str(result2)


if __name__=="__main__":
    print(nearestPalindromic("10"))
