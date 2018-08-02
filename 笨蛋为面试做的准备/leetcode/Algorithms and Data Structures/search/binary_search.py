def binary_search(lists, key):
    if lists == []:
        return -1
    if len(lists) == 1:
        if key == lists[0]:
            return 0
        else:
            return -1
    lists.sort()
    low, high = 0, len(lists)-1
    while low < high:
        mid = (low+high) // 2
        if lists[mid] > key:
            high = mid - 1
        if lists[mid] < key:
            low = mid + 1
        if lists[mid] == key:
            return mid
    return -1

if __name__=="__main__":
    print(binary_search([1,2,3], 2))