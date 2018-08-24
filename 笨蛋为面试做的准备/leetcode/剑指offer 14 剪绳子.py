def solution(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    lst = [0 for _ in range(n+1)]
    lst[:4] = [0, 1, 2, 3]

    for i in range(4, n+1):
        max = 0
        for j in range(1, i//2+1):
            temp = lst[j] * lst[i-j]
            if max < temp:
                max = temp
        lst[i] = max

    max = lst[n]
    return max

if __name__ == "__main__":
    print(solution(8))