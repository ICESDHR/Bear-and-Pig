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