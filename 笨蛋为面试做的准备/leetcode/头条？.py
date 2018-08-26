import sys


def buildstr1(Str, j):
    return Str[j:] + Str[0:j]


def buildstr2(Str, j):
    temp = ""
    for i in range(j, -1, -1):
        if i > len(Str) - 1:
            break
        temp += Str[i]
    for k in range(len(Str) - 1, j, -1):
        temp += Str[k]
    return temp


def check(lst):
    for i in range(len(lst)):
        temp = lst[i]
        templst = lst[:i] + lst[i + 1:]
        for j in range(len(temp)):
            ans1 = buildstr1(temp, j)
            ans2 = buildstr2(temp, j)
            if ans1 in templst or ans2 in templst:
                return True
    return False


if __name__ == "__main__":
    # line = sys.stdin.readline().strip()
    # n, k = list(map(str, line.split()))

    n = int(input())
    result = []
    for i in range(n):
        lst = []
        m = int(input())
        for j in range(m):
            lst.append(input())
        if check(lst):
            result.append("Yeah")
        else:
            result.append("Sad")

    for i in range(len(result)):
        print(result[i])
