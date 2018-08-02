def bubble_sort(lists):
    if len(lists) <= 1:
        return lists
    for i in range(0, len(lists)):
        for j in range(i + 1, len(lists)):
            if lists[i] > lists[j]:
                lists[j], lists[i] = lists[i], lists[j]
    return lists


if __name__ == "__main__":
    lists = [9, 8, 7, 6, 5]
    print(bubble_sort(lists))
