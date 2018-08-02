def quick_sort1(lists):
    if len(lists) <= 1:
        return lists
    left = [i for i in lists[1:] if i < lists[0]]
    right = [i for i in lists[1:] if i >= lists[0]]
    return quick_sort1(left) + [lists[0]] + quick_sort1(right)


def quick_sort2(lists):
    if len(lists) <= 1:
        return lists
    low, high = 0, len(lists) - 1
    pivot = 0
    while low < high:
        while low < high:
            if lists[pivot] > lists[high]:
                lists[high], lists[low] = lists[low], lists[high]
                pivot = high
                break
            high -= 1
        while low < high:
            if lists[pivot] < lists[low]:
                lists[high], lists[low] = lists[low], lists[high]
                pivot = low
                break
            low += 1
    return quick_sort2(lists[:pivot]) + [lists[pivot]] + quick_sort2(lists[pivot + 1:])


if __name__ == "__main__":
    lists = [9, 8, 7, 6, 5]
    print(quick_sort1(lists))
    lists = [9, 8, 7, 6, 5]
    print(quick_sort2(lists))
