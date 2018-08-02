def select_sort(lists):
    """
    简单选择排序，稳定排序，时间复杂度为 o(n^2)，查找每一次最小值的时候都要经过 n-1 次比较
    """
    length = len(lists)
    for i in range(length):
        key = i
        for j in range(i+1, length):
            if lists[key] > lists[j]:
                key = j
        lists[i], lists[key] = lists[key], lists[i]
    return lists

if __name__ == "__main__":
    lists = [9, 8, 7, 6, 5]
    print(select_sort(lists))