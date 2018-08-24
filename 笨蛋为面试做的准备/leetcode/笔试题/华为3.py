# coding=utf-8

def Compare(DNA, i, j):
    length = 0
    while j + length < len(DNA) and DNA[i + length] == DNA[j + length]:
        length += 1
    return length


def MaxSubDNA(DNA):
    ans = ''
    length = 0
    for i in range(len(DNA)):
        for j in range(i + 1 + length, len(DNA) - 1 - length):
            if DNA[i] == DNA[j]:
                temp = Compare(DNA, i, j)
                if temp > length:
                    length = temp
                    ans = DNA[i:i + length]
    return ans, length


if __name__ == "__main__":
    DNA = input()
    temp, length = MaxSubDNA(DNA)
    if length:
        print(temp, length)
    else:
        print(' 0')
