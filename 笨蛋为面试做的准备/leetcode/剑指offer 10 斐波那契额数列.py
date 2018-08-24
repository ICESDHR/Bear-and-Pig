def Fibonacci(n):
    # write code here
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    return Fibonacci(n - 1) + Fibonacci(n - 2)

def Fibonacci1(n):
    if n < 1:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 1
    pre = 1
    end = 1
    while n > 2:
        result = pre+end
        pre = end
        end = result
        n -= 1
    return result


if __name__ == "__main__":
    print(Fibonacci1(5))