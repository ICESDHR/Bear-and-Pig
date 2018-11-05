#!/bin/python
# -*- coding: utf8 -*-
import sys
import os
import re


# 请完成下面这个函数，实现题目要求的功能
# 当然，你也可以不按照下面这个模板来作答，完全按照自己的想法来 ^-^
# ******************************开始写代码******************************


def sim(sub, T):
    a = [sub.index(i) for i in sub]
    b = [T.index(i) for i in T]
    return a == b


def solve(S, T):
    if len(S) < len(T):
        return 0
    count = 0
    for i in range(0, len(S)):
        cur = S[i:i + len(T)]
        if len(cur) == len(T):
            if sim(cur, T):
                count += 1
    return count


# ******************************结束写代码******************************


try:
    _S = input()
except:
    _S = None

try:
    _T = input()
except:
    _T = None

res = solve(_S, _T)

print(str(res) + "\n")
