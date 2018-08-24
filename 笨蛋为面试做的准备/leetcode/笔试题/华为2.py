def Solution(s):
    stack = []
    tmp = [0 for _ in range(len(s))]
    for (i, ch) in enumerate(s):
        if ch == ')':
            if len(stack) == 0:
                stack.append((ch, i))
            else:
                if stack[-1][0] == '(':
                    ele = stack.pop()
                    tmp[ele[1]] = 1
                    tmp[i] = 1
                else:
                    stack.append((ch, i))
        else:
            stack.append((ch, i))
    max_counter = 0
    counter = 0
    for v in tmp:
        if v == 0:
            counter = 0
        else:
            counter += 1
            if counter > max_counter:
                max_counter = counter
    return max_counter


if __name__ == "__main__":
    tempStr = input()
    print(Solution(tempStr))
