def insert_sort(lists):
    if len(lists) <= 1:
        return lists
    for i in range(1, len(lists)):
        key = lists[i]
        j = i - 1
        while j >= 0:
            if lists[j] > key:
                lists[j + 1] = lists[j]
                lists[j] = key
            j -= 1
    return lists


if __name__ == "__main__":
    lists = [9, 8, 7, 6, 5]
    print(insert_sort(lists))
