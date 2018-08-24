import sys
if __name__ == "__main__":
    line = sys.stdin.readline().strip()
    n, k = list(map(float, line.split()))
    n = int(n)

    if n >= 3:
        result1 = n * k * 0.7
    else:
        result1 = n * k
    if result1 < 50:
        result1 += 10

    result2 = n * k
    if result2 >= 10:
        result2 -= 2 * (result2//10)
    if result2 < 99:
        result2 += 6

    result1 = round(result1, 2)
    result2 = round(result2, 2)
    # print(result1, result2)
    if result1 < result2:
        print(1)
    elif result1 > result2:
        print(2)
    else:
        print(0)