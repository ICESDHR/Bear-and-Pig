def solution(Str):
    count = 0
    for i in range(len(Str)):
        if Str[i] == " ":
            count += 1

    lst = [0 for _ in range(len(Str)+2*count)]
    temp = len(lst) - 1
    for j in range(len(Str)-1, -1, -1):
        if Str[j] == " ":
            lst[temp] = "0"
            lst[temp-1] = "2"
            lst[temp-2] = "%"
            temp = temp-3
        else:
            lst[temp] = Str[j]
            temp -= 1
    result = ""
    for k in range(len(lst)):
        result += lst[k]
    print(result)
    return lst

def replaceSpace(s):
    # write code here
    s = list(s)
    for i in range(len(s)):
        if s[i] == ' ':
            s[i] = '%20'
    return ''.join(s)

if __name__ == "__main__":
    print(replaceSpace("we are"))