def bucket_sort(lists):
    """
    桶排序，非比较模型，适用于数据量非常大，数据紧凑，相同数据很多的情况，比如统计每年高考学生的分数
    """
    if lists == [] or len(lists) == 1:
        return lists
    mini = min(lists)  # 查找方法
    maxi = max(lists)
    bucket = []
    for _ in range(0, maxi + 1 - mini):
        bucket.append(0)
    for i in lists:
        bucket[i - mini] += 1
    res = []
    for i in range(0, len(bucket)):
        while bucket[i] > 0:
            res.append(i + mini)
            bucket[i] -= 1
    return res


if __name__ == "__main__":
    lists = [9, 8, 7, 6, 5]
    print(bucket_sort(lists))
