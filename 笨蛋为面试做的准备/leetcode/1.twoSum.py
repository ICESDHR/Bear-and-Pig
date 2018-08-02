def twoSum(nums, target):
    lookup = {}
    for i, num in enumerate(nums):
        if target - num in lookup:
            return [lookup[target - num], i]
        lookup[num] = i

if __name__=="__main__":
    nums = [2, 7, 11, 15]
    target = 9
    print(twoSum(nums, target))