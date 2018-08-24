def NumberOf1(n):
    # write code here
    count = 0
    n = n & 0xffffffff
    while n:
        count += 1
        n = (n - 1) & n
    return count

if __name__ == "__main__":
    print(bin(3))