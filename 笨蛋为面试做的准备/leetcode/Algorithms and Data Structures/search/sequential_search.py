def sequential_search(lists, key):
    for i in range(len(lists)):
        if lists[i] == key:
            return i
    return -1

if __name__=="__main__":
    print(sequential_search([1,2,3], 2))