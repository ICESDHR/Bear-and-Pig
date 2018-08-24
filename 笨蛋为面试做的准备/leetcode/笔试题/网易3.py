# coding=utf-8
import sys
from scipy.special import comb


def Function(m, n, k):
    count = 1
    for i in range(m):
        if k > count:
            count += comb(n + i, i + 1)
        else:
            count -= comb(n + i - 1, i)
            print('a' * (m - i) + 'z', end='')
            Function(i, n - 1, k - count)
            return
        print('-1')


if __name__ == "__main__":
    # line = sys.stdin.readline().strip()
    # n, m, k = list(map(int, line.split()))
    Function(2, 2, 4)
