def radix_sort(lists):
    """
    基数排序，针对“正整数”来写的算法函数，稳定排序，按照千位、百位、十位来排序
    """
    import math
    k = int(math.ceil(math.log(max(lists), 10)))
    bucket = [[] for _ in range(10)]
    for i in range(1, k + 1):
        for j in lists:
            # num =
            bucket[(j % (10 ** i)) // 10 ** (i - 1)].append(j)
        del lists[:]
        for z in bucket:
            lists += z
            del z[:]
    return lists


if __name__ == "__main__":
    lists = [9, 8, 7, 6, 5]
    print(radix_sort(lists))